import pygame
import sys
from enum import Enum
from settings import INTERNAL_WIDTH, INTERNAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, FPS, TILE_SIZE, ROOM_ROWS, ROOM_COLS
from src.input import Input
from src.camera import Camera
from src.rooms.room import Room
from src.entities.player import Player
from src.entities.npc import NpcManager
from src.systems.inventory import Inventory
from src.systems.dialogue import DialogueSystem
from src.ui.hud import HUD
from src.ui.menus import InventoryScreen
from src.ui.dialogue_box import DialogueBox

class GameState(Enum):
    PLAYING = 1
    TRANSITIONING = 2
    PAUSED = 3
    DIALOGUE = 4
    INVENTORY = 5
    QUIT = 6

class Engine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.internal = pygame.Surface((INTERNAL_WIDTH, INTERNAL_HEIGHT))
        pygame.display.set_caption("A Goblin's Quest")
        self.clock = pygame.time.Clock()
        self.input = Input()
        self.camera = Camera()
        self.state = GameState.PLAYING
        self.running = True

        self.npc_manager = NpcManager()
        self.item_defs = Inventory.load_definitions()
        self.inventory = Inventory()
        self.dialogue = DialogueSystem()
        self.hud = HUD()
        self.inv_screen = InventoryScreen()
        self.dialogue_box = DialogueBox()

        self.met_npcs = set()
        self.puzzles_done = set()

        self.current_room_id = "village_01"
        self.current_room = Room(self.current_room_id, self.npc_manager, self.item_defs)
        player_height = 32
        spawn_y = self._find_ground(32, self.current_room, player_height)
        self.player = Player(32, spawn_y)
        self.transition_data = None
        self.transition_timer = 0.0

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            self._handle_events(dt)
            if self.state == GameState.PLAYING:
                self._update_playing(dt)
            elif self.state == GameState.TRANSITIONING:
                self._update_transition(dt)
            elif self.state == GameState.DIALOGUE:
                self._update_dialogue(dt)
            elif self.state in (GameState.PAUSED, GameState.INVENTORY):
                pass
            self._render()
            self._end_frame()
        pygame.quit()
        sys.exit()

    def _handle_events(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == GameState.PLAYING:
                        self.state = GameState.PAUSED
                    elif self.state == GameState.PAUSED:
                        self.state = GameState.PLAYING
                    elif self.state == GameState.INVENTORY:
                        self.state = GameState.PLAYING
                    elif self.state == GameState.DIALOGUE:
                        self._advance_dialogue()
                        return
                if event.key == pygame.K_e and self.state == GameState.PLAYING:
                    self._try_interact()
                if event.key == pygame.K_i:
                    if self.state == GameState.PLAYING:
                        self.state = GameState.INVENTORY
                        self.inv_screen.selected = 0
                    elif self.state == GameState.INVENTORY:
                        self.state = GameState.PLAYING
            self.input.handle_event(event)

    def _end_frame(self):
        self.input.update()

        if self.state == GameState.DIALOGUE:
            if (self.input.is_key_just_pressed(pygame.K_SPACE) or
                self.input.is_key_just_pressed(pygame.K_e)):
                self._advance_dialogue()

    def _try_interact(self):
        px = self.player.rect.centerx
        py = self.player.rect.centery
        for npc in self.current_room.npcs:
            dx = abs(npc.rect.centerx - px)
            dy = abs(npc.rect.centery - py)
            if dx < npc.interact_range and dy < npc.interact_range:
                self._start_dialogue(npc)
                return
        for item in self.current_room.items:
            if item.collected:
                continue
            if self.player.rect.colliderect(item.rect):
                self._pickup_item(item)
                return

    def _start_dialogue(self, npc):
        self.met_npcs.add(npc.id)
        game_state = {
            "inventory": self.inventory,
            "met_npcs": self.met_npcs,
            "puzzles_done": self.puzzles_done,
        }
        self.dialogue.start(npc.id, npc.name, game_state)
        if self.dialogue.current_tree:
            self.state = GameState.DIALOGUE

    def _advance_dialogue(self):
        actions = self.dialogue.advance()
        if actions:
            for action_type, value in actions:
                self._handle_dialogue_action(action_type, value)
        if self.dialogue.finished:
            self.state = GameState.PLAYING

    def _update_dialogue(self, dt):
        self.dialogue.update(dt)

    def _handle_dialogue_action(self, action_type, value):
        if action_type == "give_item":
            self.inventory.add(value)
        elif action_type == "remove_item":
            self.inventory.remove(value)
        elif action_type == "action":
            if value.startswith("solve_puzzle_"):
                puzzle_id = value.replace("solve_puzzle_", "")
                self.puzzles_done.add(puzzle_id)

    def _process_pending_actions(self):
        if not self.dialogue.pending_actions:
            return
        for action_type, value in self.dialogue.pending_actions:
            self._handle_dialogue_action(action_type, value)
        self.dialogue.pending_actions = []

    def _pickup_item(self, item):
        if self.inventory.add(item.item_id):
            item.collected = True

    def _update_playing(self, dt):
        self.player.update(dt, self.input, self.current_room)
        exit_data = self.player.check_exit(self.current_room)
        if exit_data:
            self._start_transition(exit_data)

    def _start_transition(self, exit_data):
        self.transition_data = exit_data
        self.state = GameState.TRANSITIONING
        self.transition_timer = 0.0

    def _find_ground(self, x, room, player_height):
        col = x // TILE_SIZE
        if col < 0:
            col = 0
        if col >= ROOM_COLS:
            col = ROOM_COLS - 1
        for row in range(ROOM_ROWS):
            if room.collision[row][col] > 0:
                return row * TILE_SIZE - player_height
        return (ROOM_ROWS - 2) * TILE_SIZE

    def _update_transition(self, dt):
        self.transition_timer += dt
        if self.transition_timer >= 0.15:
            exit_data = self.transition_data
            target = exit_data["target"]
            direction = exit_data["direction"]
            self.current_room_id = target
            self.current_room = Room(target, self.npc_manager, self.item_defs)
            self.player.vy = 0.0
            spawn_x = 4
            if direction == "right":
                spawn_x = 4
            elif direction == "left":
                spawn_x = self.current_room.width - self.player.rect.w - 4
            elif direction == "down":
                spawn_x = self.current_room.width // 2
                self.player.rect.y = 4
            elif direction == "up":
                spawn_x = self.current_room.width // 2
                self.player.rect.y = self.current_room.height - self.player.rect.h - 4
            self.player.rect.x = spawn_x
            if direction in ("left", "right"):
                self.player.rect.y = self._find_ground(spawn_x, self.current_room, self.player.rect.height)
            self.state = GameState.PLAYING
            self.transition_data = None

    def _render(self):
        self.internal.fill((20, 24, 40))
        if self.state in (GameState.PLAYING, GameState.TRANSITIONING, GameState.PAUSED, GameState.DIALOGUE):
            self.current_room.render(self.internal, self.camera)
            self.player.render(self.internal, self.camera)
            self.hud.render(self.internal, self.player, self.inventory, self.item_defs)
            if self.state == GameState.DIALOGUE:
                node = self.dialogue._current_node()
                if node:
                    self.dialogue_box.render(
                        self.internal,
                        self.dialogue.active_npc_name,
                        self.dialogue.current_text(),
                        self.dialogue.text_complete(),
                        self.dialogue.awaiting_input
                    )
            elif self.state == GameState.PAUSED:
                pause_font = pygame.font.SysFont("Consolas", 20, bold=True)
                text = pause_font.render("PAUSED", True, (200, 190, 160))
                self.internal.blit(text, (INTERNAL_WIDTH // 2 - text.get_width() // 2, INTERNAL_HEIGHT // 2 - 10))
        elif self.state == GameState.INVENTORY:
            self.current_room.render(self.internal, self.camera)
            self.player.render(self.internal, self.camera)
            self.inv_screen.render(self.internal, self.inventory, self.item_defs)
        scaled = pygame.transform.scale(self.internal, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.blit(scaled, (0, 0))
        pygame.display.flip()
