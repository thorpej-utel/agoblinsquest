# A Goblin's Quest

A room-to-room fantasy adventure platformer built with Pygame, inspired by classic Codemasters Dizzy titles and late-80s/early-90s home computer adventures.

## Premise

The Goblin King has vanished beneath Blackfang Mountain, searching for the mythical Crown of Endless Riches. When the tribe's greatest warriors fail to return, a young maintenance goblin named **Grub** accidentally becomes the kingdom's last hope. Armed with little more than determination and questionable common sense, his journey begins.

## Features

- **30+ interconnected rooms** across 6 distinct regions (Goblin Village, Mushroom Woods, Old Watchtower, Troll Marsh, Blackfang Mountain, Forgotten Depths)
- **Exploration-driven gameplay** — discover items, meet NPCs, solve environmental puzzles, unlock new areas
- **Inventory system** — manage up to 6 items, use and combine them to solve puzzles
- **NPCs and dialogue** — talk to quirky characters, trade items, advance the story
- **Light platforming** — jump, climb, dodge hazards, and navigate classic room-to-room transitions
- **Heart-based health** — avoid enemies and hazards, collect food to restore health
- **Secrets and collectibles** — find hidden rooms, Gold Teeth, and joke items
- **Data-driven design** — all rooms, items, NPCs, dialogue, and puzzles defined in JSON

## Tech Stack

| Layer | Choice |
|---|---|
| Language | Python 3.11+ |
| Engine | Pygame Community Edition (`pygame-ce`) |
| Config/Data | JSON |
| Sprites | Pixel art (Aseprite → sprite sheets) |
| Audio | WAV/OGG via Pygame mixer |

## Getting Started

```bash
# Clone the repository
git clone <repo-url>
cd agoblinsquest

# Create a virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install pygame-ce

# Run the game
python main.py
```

## Controls

| Key | Action |
|---|---|
| Arrow keys / WASD | Move / Climb |
| Space | Jump |
| E | Interact / Pick up |
| I | Open inventory |
| M | Map (if available) |
| Escape | Pause |

## Project Structure

```
agoblinsquest/
├── main.py              # Entry point
├── settings.py          # Game configuration
├── src/                 # Game source code
│   ├── engine.py        # Game loop & state machine
│   ├── input.py         # Input handling
│   ├── camera.py        # Scrolling camera
│   ├── rooms/           # Room system
│   ├── entities/        # Player, NPCs, enemies
│   ├── systems/         # Physics, inventory, puzzles, etc.
│   ├── ui/              # HUD, menus, dialogue
│   └── utils/           # Animation, helpers
├── data/                # JSON content files
├── assets/              # Sprites, tilesets, audio
└── saves/               # Save files
```

## Development Roadmap

1. **Foundation** — Game loop, player movement, physics, room transitions
2. **Content Pipeline** — Inventory, NPCs, dialogue, HUD
3. **Gameplay Systems** — Puzzles, enemies, health, save system
4. **Content Expansion** — Build all 30 rooms, items, and puzzles
5. **Endgame** — Boss encounter, cutscenes, victory
6. **Polish** — Sprites, audio, visual juice, balancing

## Status

Early development. See [PLAN.md](PLAN.md) and [TASKS.md](TASKS.md) for details.
