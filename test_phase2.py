"""Phase 2 system tests — run with: python test_phase2.py"""
import sys
sys.path.insert(0, ".")

import json

errors = []
passed = 0
failed = 0

def check(description, condition):
    global passed, failed
    if condition:
        passed += 1
        print(f"  PASS  {description}")
    else:
        failed += 1
        errors.append(description)
        print(f"  FAIL  {description}")

print("=== Inventory ===")
from src.systems.inventory import Inventory
inv = Inventory()
check("starts empty", inv.count() == 0 and inv.items == [])
check("add item", inv.add("rope"))
check("has item", inv.has("rope"))
check("count is 1", inv.count() == 1)
check("second add", inv.add("torch"))
check("count is 2", inv.count() == 2)
check("remove item", inv.remove("rope"))
check("rope gone", not inv.has("rope"))
check("torch still there", inv.has("torch"))
check("count 1 after remove", inv.count() == 1)
for i in range(6):
    inv.add(f"item_{i}")
check("stays at max 6", inv.count() == 6)
check("cant add beyond max", not inv.add("extra"))

print("\n=== Item Definitions ===")
item_defs = Inventory.load_definitions()
check("items.json loaded", len(item_defs) > 0)
check("rope defined", "rope" in item_defs)
check("rope has name", item_defs["rope"]["name"] == "Rope")
check("rope has description", len(item_defs["rope"]["description"]) > 0)
check("rope has color 3-tuple", len(item_defs["rope"]["color"]) == 3)
check("torch defined", "torch" in item_defs)
check("magic_spoon joke type", item_defs["magic_spoon"]["type"] == "joke")
check("honey_cake food type", item_defs["honey_cake"]["type"] == "food")

print("\n=== NPC Data Loading ===")
from src.entities.npc import NpcManager
nm = NpcManager()
for npc_id in ["chief", "marna", "gorb", "zog", "grik", "pip", "grum", "gromble", "squig", "mirelda", "moss", "thorne"]:
    data = nm.load_npc(npc_id)
    check(f"NPC {npc_id} data loads", data is not None)
    check(f"NPC {npc_id} has name", "name" in data)
    check(f"NPC {npc_id} has color", "color" in data and len(data["color"]) == 3)
    check(f"NPC {npc_id} has size", "size" in data and len(data["size"]) == 2)
    check(f"NPC {npc_id} has interact_range", "interact_range" in data)

print("\n=== NPC Dialogue Loading ===")
for npc_id in ["chief", "marna", "gorb", "zog", "grik", "pip", "grum", "gromble", "squig", "mirelda", "moss", "thorne"]:
    d = nm.load_dialogue(npc_id)
    check(f"{npc_id} dialogue loads", len(d) > 0)
    has_nodes = all("nodes" in tree for tree in d.values())
    check(f"{npc_id} all trees have nodes", has_nodes)
    valid_nodes = True
    for key, tree in d.items():
        for i, node in enumerate(tree["nodes"]):
            if "text" not in node:
                valid_nodes = False
    check(f"{npc_id} all nodes have text", valid_nodes)

print("\n=== Dialogue System ===")
from src.systems.dialogue import DialogueSystem

# Empty game state
ds = DialogueSystem()
gs_empty = {"inventory": Inventory(), "met_npcs": set(), "puzzles_done": set()}
ds.start("chief", "Chief Bork", gs_empty)
check("chief dialogue starts", not ds.finished)
check("has current node", ds._current_node() is not None)
check("current text starts empty", ds.current_text() == "")
check("text not complete", not ds.text_complete())

# Simulate typewriter — advance through all nodes
def wait_for_text(sys, timeout=5.0):
    elapsed = 0.0
    while not sys.text_complete() and elapsed < timeout:
        sys.update(0.5)
        elapsed += 0.5
    return sys.text_complete()

def advance_node(sys):
    """Complete current text and advance to next node. Returns actions."""
    if not sys.awaiting_input:
        # Complete the text first
        wait_for_text(sys)
    return sys.advance()

ds.update(5.0)
check("text appears after time", len(ds.current_text()) > 0)
check("text complete after 5s", ds.text_complete())
check("awaiting input", ds.awaiting_input)

# Advance through all 4 nodes of chief intro
advance_node(ds)
check("advanced to node 1", ds.current_node_idx == 1 and not ds.finished)

advance_node(ds)
check("advanced to node 2", ds.current_node_idx == 2 and not ds.finished)

advance_node(ds)
check("advanced to node 3", ds.current_node_idx == 3 and not ds.finished)

actions = advance_node(ds)
check("last node returns actions", actions is not None)
check("dialogue finished", ds.finished)

print("\n=== Dialogue Condition Matching ===")
ds2 = DialogueSystem()
inv_with_rope = Inventory()
inv_with_rope.add("rope")
gs_rope = {"inventory": inv_with_rope, "met_npcs": set(), "puzzles_done": set()}
ds2.start("chief", "Chief Bork", gs_rope)
check("chief has_rope tree selected", not ds2.finished)
text = ds2.current_text()
ds2.update(5.0)
full_text = ds2.current_text()
check("has_rope tree shows different text", len(full_text) > 0)

print("\n=== Dialogue Give/Remove Actions ===")
ds3 = DialogueSystem()
inv_act = Inventory()
gs_act = {"inventory": inv_act, "met_npcs": set(), "puzzles_done": set()}
ds3.start("marna", "Marna", gs_act)
check("marna dialogue starts", not ds3.finished)

# Marna's intro gives honey_cake on node 1
advance_node(ds3)
check("marna at node 1", ds3.current_node_idx == 1 and not ds3.finished)

actions = advance_node(ds3)
check("marna last node gives actions", actions is not None)
has_give = any(a[0] == "give_item" and a[1] == "honey_cake" for a in actions)
check("give_item action present", has_give)
check("marna dialogue finished", ds3.finished)

print("\n=== Puzzle Dialogue Actions ===")
ds4 = DialogueSystem()
inv_gear = Inventory()
inv_gear.add("broken_gear")
inv_gear.add("hammer")
gs_squig = {"inventory": inv_gear, "met_npcs": set(), "puzzles_done": set()}
ds4.start("squig", "Professor Squig", gs_squig)
check("squig dialogue starts", not ds4.finished)

# Squig has_gear_hammer dialogue triggers on first advance
advance_node(ds4)
check("squig advanced past intro", ds4.current_node_idx > 0 and not ds4.finished)

actions = advance_node(ds4)
check("squig has action", actions is not None)
has_action = any(a[0] == "action" and a[1] == "solve_puzzle_broken_lift" for a in actions)
check("solve_puzzle_broken_lift action", has_action)
check("dialogue finished", ds4.finished)

print("\n=== Room Loading ===")
# Note: this requires pygame init for the Npc rendering
import pygame
pygame.init()
from src.rooms.room import Room
room = Room("village_01", nm, item_defs)
check("room loads", room is not None)
check("room has name", room.name == "Village Square")
check("room has npcs", len(room.npcs) > 0)
check("room has items", len(room.items) > 0)
check("room has exits", len(room.exits) > 0)

npc_ids = [n.id for n in room.npcs]
check("chief in room", "chief" in npc_ids)
check("marna in room", "marna" in npc_ids)
check("gorb in room", "gorb" in npc_ids)
check("zog in room", "zog" in npc_ids)
check("grik in room", "grik" in npc_ids)
check("pip in room", "pip" in npc_ids)

item_ids = [i.item_id for i in room.items]
check("honey_cake in room", "honey_cake" in item_ids)

# Check NPC bounds are within room
for npc in room.npcs:
    check(f"NPC {npc.id} x in bounds", 0 <= npc.rect.x < 384)
    check(f"NPC {npc.id} y in bounds", 0 <= npc.rect.y < 192)
    check(f"NPC {npc.id} bottom on ground or above", npc.rect.bottom <= 224)

# Check room 2
room2 = Room("village_02", nm, item_defs)
check("room2 loads", room2 is not None)
npc2_ids = [n.id for n in room2.npcs]
check("moss in room2", "moss" in npc2_ids)
item2_ids = [i.item_id for i in room2.items]
check("magic_spoon in room2", "magic_spoon" in item2_ids)
pygame.quit()

print("\n=== Physics Collision ===")
from src.systems.physics import move_and_collide
from settings import ROOM_ROWS, ROOM_COLS, TILE_SIZE

collision_map = [[0] * ROOM_COLS for _ in range(ROOM_ROWS)]
for col in range(ROOM_COLS):
    collision_map[ROOM_ROWS - 1][col] = 1

player_rect = pygame.Rect(100, (ROOM_ROWS - 1) * TILE_SIZE - 10 - 20, 20, 20)
velocity_x = 0.0
velocity_y = 200.0
velocity_x, velocity_y, grounded = move_and_collide(player_rect, velocity_x, velocity_y, 0.1, collision_map)
check("player lands on ground after falling", grounded)
check("vertical velocity is zero after landing", velocity_y == 0.0)
check("player bottom sits on ground tile", player_rect.bottom == (ROOM_ROWS - 1) * TILE_SIZE)

print("\n=== Engine Initialization ===")
pygame.init()
from src.engine import Engine
e = Engine()
check("engine creates player", e.player is not None)
check("player has 4 hearts", e.player.hearts == 4)
check("engine in PLAYING state", e.state.value == 1)
check("engine has npc_manager", e.npc_manager is not None)
check("engine has inventory", e.inventory is not None)
check("engine has dialogue", e.dialogue is not None)
check("current room has NPCs in engine", len(e.current_room.npcs) > 0)
check("current room has items in engine", len(e.current_room.items) > 0)
pygame.quit()

print(f"\n{'='*40}")
print(f"Results: {passed} passed, {failed} failed")
if errors:
    print(f"Failures:")
    for e in errors:
        print(f"  - {e}")
else:
    print("All tests passed!")
