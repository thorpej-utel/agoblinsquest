import json
import pygame

CHAR_RATE = 30

class DialogueSystem:
    def __init__(self):
        self.active_npc = None
        self.active_npc_name = ""
        self.dialogues = {}
        self.current_tree = None
        self.current_node_idx = 0
        self.char_index = 0
        self.char_timer = 0.0
        self.awaiting_input = False
        self.finished = True
        self.pending_actions = []

    def start(self, npc_id, npc_name, game_state):
        self.active_npc = npc_id
        self.active_npc_name = npc_name
        with open(f"data/npcs/{npc_id}/dialogue.json") as f:
            self.dialogues = json.load(f)
        self.current_tree = self._find_best_tree(game_state)
        self.current_node_idx = 0
        self.char_index = 0
        self.char_timer = 0.0
        self.awaiting_input = False
        self.finished = False
        self.pending_actions = []

    def _find_best_tree(self, game_state):
        best = None
        best_priority = -1
        for key, tree in self.dialogues.items():
            conds = tree.get("conditions", {})
            if self._check_conditions(conds, game_state):
                priority = tree.get("priority", 0)
                if priority >= best_priority:
                    best = key
                    best_priority = priority
        if best:
            return self.dialogues[best]
        return None

    def _check_conditions(self, conds, game_state):
        for key, value in conds.items():
            if key == "has_item":
                if not game_state["inventory"].has(value):
                    return False
            elif key == "not_has_item":
                if game_state["inventory"].has(value):
                    return False
            elif key == "has_met":
                if value not in game_state.get("met_npcs", set()):
                    return False
            elif key == "puzzle_done":
                if value not in game_state.get("puzzles_done", set()):
                    return False
        return True

    def update(self, dt):
        if self.finished or self.awaiting_input:
            return
        self.char_timer += dt
        chars_to_add = int(self.char_timer * CHAR_RATE)
        if chars_to_add > 0:
            self.char_index += chars_to_add
            self.char_timer -= chars_to_add / CHAR_RATE
        node = self._current_node()
        if node and self.char_index >= len(node["text"]):
            self.char_index = len(node["text"])
            self.awaiting_input = True

    def advance(self):
        if not self.awaiting_input:
            self.char_index = len(self._current_node()["text"])
            self.awaiting_input = True
            return None
        node = self._current_node()
        actions = []
        if "give_item" in node:
            actions.append(("give_item", node["give_item"]))
        if "remove_item" in node:
            actions.append(("remove_item", node["remove_item"]))
        if "action" in node:
            actions.append(("action", node["action"]))
        next_idx = node.get("next")
        if next_idx is None:
            self.finished = True
            self.pending_actions = actions
            return actions
        self.current_node_idx = next_idx
        self.char_index = 0
        self.char_timer = 0.0
        self.awaiting_input = False
        self.pending_actions = actions
        return actions

    def _current_node(self):
        if not self.current_tree:
            return None
        nodes = self.current_tree.get("nodes", [])
        if self.current_node_idx < len(nodes):
            return nodes[self.current_node_idx]
        return None

    def current_text(self):
        node = self._current_node()
        if not node:
            return ""
        return node["text"][:self.char_index]

    def text_complete(self):
        node = self._current_node()
        return node and self.char_index >= len(node["text"])
