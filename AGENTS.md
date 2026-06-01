# A Goblin's Quest — AGENTS.md

## Project state

Fresh project — **no code written yet**. All existing files are planning/docs:
`PLAN.md`, `TASKS.md`, `PRD.md`, `README.md`, `requirements.txt`, `LICENSE`.

## Quickstart

```powershell
.venv\Scripts\activate      # venv already exists
pip install -r requirements.txt   # installs pygame-ce
python main.py               # run game (once it exists)
```

## Architecture (from PLAN.md)

- **Pygame Community Edition** (`pygame-ce`) — not regular Pygame. Import as `pygame`.
- **Room size**: 384x216 at 16px tiles (24x14 grid). Display at 2x scale = 768x432.
- **Custom AABB physics** — no physics engine. Simple gravity, no slopes.
- **Data-driven**: all content in `data/` as JSON (rooms, items, NPCs, dialogue, puzzles, enemies).
- **Screen-edge exits**: walking past left/right/top/bottom edge triggers room transition (Dizzy-style).
- **Player sprite**: 48x64 or 64x64. Use placeholder rectangles until Phase 6.
- **Save format**: JSON — inventory, current room, puzzle states, health, position.

## Code structure

```
main.py            # entry point
settings.py        # constants, paths, config
src/
  engine.py        # game loop + state machine (TITLE/PLAYING/PAUSED/DIALOGUE/INVENTORY/MAP/CUTSCENE/GAME_OVER)
  input.py         # keyboard handler
  camera.py        # world-to-screen transform
  rooms/           # manager.py, room.py, tilemap.py
  entities/        # player.py, npc.py, enemy.py
  systems/         # physics.py, inventory.py, puzzle.py, dialogue.py, save.py
  ui/              # hud.py, menus.py, dialogue_box.py
  utils/           # animation.py, helpers.py
data/              # JSON: rooms/*.json, items.json, npcs.json, dialogues.json, puzzles.json, enemies.json
assets/            # sprites/, tilesets/, backgrounds/, fonts/, sfx/, music/
saves/             # runtime save files (gitignored)
```

## Development workflow

- **Follow TASKS.md** in order — phases are sequential and each depends on the previous.
- **Phase 1 first**: game loop, state machine, input, camera, tilemap rendering, player movement, physics, room transitions.
- **Placeholders until Phase 6**: use colored rectangles/shapes for player, NPCs, enemies.
- **All content in JSON**: never hardcode room layouts, item definitions, NPC positions, dialogue, or puzzle logic in Python files.
- **Story & NPC content**: designed in `data/story_and_npcs.md`, data files (dialogues.json, npcs.json) generated from it.

## Key conventions

- Import pygame-ce as `import pygame` (same import name as regular Pygame).
- Room JSON uses `"exits"` array with direction/target/x/y.
- Inventory limited to 6 items max.
- Health: 4 hearts, contact damage, food restores.
- Tile size: 16x16 pixels.
- No slopes, no rotating platforms — keep collision simple (AABB).
