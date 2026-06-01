# A Goblin's Quest — Development Plan

## Overview

A room-to-room fantasy adventure platformer in Pygame, inspired by classic Codemasters Dizzy titles. ~30 rooms, 10-12 NPCs, ~20 puzzle items, ~30 secrets.

---

## Tech Stack

| Layer | Choice |
|---|---|
| Language | Python 3.11+ |
| Engine | Pygame Community Edition (`pygame-ce`) |
| Config/Data | JSON files (rooms, items, NPCs, dialogue) |
| Sprites | Aseprite → sprite sheets (PNG) |
| Audio | Pygame mixer (WAV/OGG) |
| Maps | Tiled `.tmx` or custom JSON tilemaps |

Reasoning: `pygame-ce` is the maintained fork of Pygame with better performance, scaled-blit support, and active development.

---

## Architecture

### Game States (FSM)

```
TITLE -> PLAYING -> PAUSED
                -> DIALOGUE
                -> INVENTORY
                -> MAP
                -> CUTSCENE
              -> GAME_OVER -> TITLE
```

### Core Loop

```
Handle Input -> Update State -> Render Frame -> Cap FPS
```

### Component Tree

```
Game
├── Engine (main loop, state machine, clock)
├── Rooms
│   ├── RoomManager (load, unload, transition)
│   ├── Room (tiles, collisions, objects, exits)
│   └── RoomRenderer (camera, parallax)
├── Entities
│   ├── Player (movement, animation, inventory)
│   ├── NPC (dialogue, quest state)
│   └── Enemy (AI behaviour, patrol)
├── Systems
│   ├── Physics (gravity, collision detection)
│   ├── Input (keyboard mapping, rebindable)
│   ├── Inventory (item grid, use, combine)
│   ├── Puzzle (condition checker, triggers)
│   ├── Dialogue (typewriter text, choices)
│   └── Save (auto/manual serialization)
├── UI
│   ├── HUD (hearts, items, gold teeth)
│   ├── InventoryScreen
│   ├── DialogueBox
│   ├── PauseMenu
│   ├── MapScreen
│   └── TitleScreen
└── Assets
    ├── sprites/
    ├── tilesets/
    ├── backgrounds/
    ├── fonts/
    ├── sfx/
    └── music/
```

---

## File Structure

```
agoblinsquest/
├── main.py                  # Entry point
├── settings.py              # Constants, paths, config
├── src/
│   ├── engine.py            # Game loop, state machine
│   ├── input.py             # Input handler
│   ├── camera.py            # Scrolling camera
│   ├── rooms/
│   │   ├── manager.py       # Room loading & transitions
│   │   ├── room.py          # Room data & collisions
│   │   └── tilemap.py       # Tile renderer
│   ├── entities/
│   │   ├── player.py        # Player controller
│   │   ├── npc.py           # NPC logic
│   │   └── enemy.py         # Enemy AI
│   ├── systems/
│   │   ├── physics.py       # Movement & collisions
│   │   ├── inventory.py     # Item management
│   │   ├── puzzle.py        # Puzzle conditions
│   │   ├── dialogue.py      # Dialogue system
│   │   └── save.py          # Save/load
│   ├── ui/
│   │   ├── hud.py           # Heads-up display
│   │   ├── menus.py         # Pause, inventory, etc.
│   │   └── dialogue_box.py  # Dialogue rendering
│   └── utils/
│       ├── animation.py     # Sprite sheet handler
│       └── helpers.py       # Math, file I/O, etc.
├── data/
│   ├── rooms/               # Room JSON files
│   │   ├── village_01.json
│   │   └── ...
│   ├── items.json           # Item definitions
│   ├── npcs.json            # NPC definitions
│   ├── dialogues.json       # All dialogue trees
│   ├── puzzles.json         # Puzzle definitions
│   └── enemies.json         # Enemy definitions
├── assets/
│   ├── sprites/             # Sprite sheets
│   ├── tilesets/            # Tile images
│   ├── backgrounds/         # Static backdrop images
│   ├── fonts/               # Pixel fonts
│   ├── sfx/                 # Sound effects (WAV)
│   └── music/               # Music tracks (OGG)
└── saves/                   # Save files (created at runtime)
```

---

## Phase 1 — Foundation (Week 1-2)

Goal: Playable prototype with a single room, player movement, and collisions.

### Milestones

1. **Project scaffold**
   - `main.py` with game loop template
   - `settings.py` with screen size, FPS, paths
   - `pygame-ce` virtual environment setup

2. **Game state machine**
   - `engine.py` — state transitions, tick & render dispatch

3. **Input handler**
   - `input.py` — key mapping, press/release detection, DAS

4. **Camera & rendering**
   - `camera.py` — world-to-screen coordinate transform

5. **Room system (minimal)**
   - `room.py` + `tilemap.py` — load a JSON room, render tiles
   - Room size: 384×216 (scaled 2x = 768×432)
   - Tile grid for collisions

6. **Player entity**
   - `player.py` — movement (left/right/jump), gravity, tile collision
   - Placeholder green rectangle as "Grub"
   - Screen-edge room transition (left/right/up/down)

7. **Physics system**
   - `physics.py` — gravity, platform collision, one-way platforms

### Deliverable
> A green rectangle walks around a single room, jumps on platforms, and transitions to a second empty room via the right edge.

---

## Phase 2 — Content Pipeline (Week 3-4)

Goal: Data-driven rooms, items, inventory, and NPC encounters.

### Milestones

1. **Room data schema**
   - JSON format: tiles (2D layer arrays), collision map, objects, exits, background
   - Room editor helper or Tiled export pipeline

2. **Multiple rooms**
   - Goblin Village starter set (4-6 rooms)
   - Room transitions with proper camera scroll

3. **Item system**
   - `items.json` — types, names, descriptions
   - Pickup & render in world
   - Inventory UI (grid, max 6)
   - Item use (context-sensitive)

4. **Inventory screen**
   - Full-screen overlay with item grid
   - Select, examine, combine, drop

5. **NPCs**
   - `npcs.json` — name, sprite, position, dialogue ID
   - `npc.py` — render, interaction zone
   - Simple dialogue trigger

6. **Dialogue system**
   - `dialogue.py` — typewriter text, page advancement
   - `dialogues.json` — tree structure with options

7. **HUD**
   - Hearts display (top-left)
   - Item slots (top-right)
   - Gold Tooth counter

### Deliverable
> Player explores several village rooms, picks up items, talks to NPCs with dialogue boxes, and opens inventory.

---

## Phase 3 — Gameplay Systems (Week 5-6)

Goal: Puzzles, enemies, hazards, and health.

### Milestones

1. **Puzzle system**
   - `puzzles.json` — conditions (item required, NPC state, etc.)
   - Triggerable objects (levers, doors, bridges)
   - On-puzzle-complete: unlock exit, spawn item, change room

2. **Enemies**
   - `enemies.json` — type, patrol path, behaviour
   - `enemy.py` — bat (fly), spider (patrol), troll (block)
   - Contact damage (removes heart)

3. **Health system**
   - 4 hearts, damage invulnerability frames
   - Food items restore health
   - Death returns to last checkpoint room, retains items

4. **Checkpoints**
   - Auto-save on room entry (certain rooms)
   - `save.py` — JSON serialization of inventory, health, position, solved puzzles

5. **Hazards**
   - Spikes, toxic pools, falling platforms
   - Moving platforms (simple sine-wave or waypoint)

### Deliverable
> Player collects items, solves a puzzle (e.g. give mushroom to troll → get key), takes damage from enemies, dies and respawns, and progresses to a locked-door room.

---

## Phase 4 — Content Expansion (Week 7-8)

Goal: Build out the world — all regions, ~30 rooms total.

### Room distribution

| Region | Rooms | Key Features |
|---|---|---|
| Goblin Village | 5 | Huts, market, tutorial NPCs, basic items |
| Mushroom Woods | 5 | Giant mushrooms, spiders, hidden caves, rope puzzle |
| Old Watchtower | 3 | Vertical climb, ladders, collapsing floor, treasure |
| Troll Marsh | 5 | Toxic pools, moving platforms, troll NPCs, mushroom trade puzzle |
| Blackfang Mountain | 6 | Mines, ruins, haunted armour, gear/hammer lift puzzle |
| Forgotten Depths | 4 | Final dungeon, lost king, boss encounter, Crown |
| Transitional caves | 2 | Connector rooms between regions |

### Milestones

1. **Region building**
   - Design all 30 rooms with JSON data
   - Each region has distinct tileset & background
   - Interconnected via screen-edge exits

2. **Item expansion**
   - Core items: Rope, Torch, Mushroom, Key, Hammer, Gear, Gemstone, Golden Acorn, Crystal Lens, Ancient Coin
   - ~20 items total

3. **Puzzles integration**
   - Broken Bridge (Rope + Plank)
   - Hungry Troll (Mushroom → Key)
   - Broken Lift (Gear + Hammer)
   - Dark Cave (Torch reveals path)
   - Locked Shrine (3 relics → progression)

4. **Secrets**
   - ~30 hidden Gold Teeth, secret passages, joke items

5. **Map system** (optional)
   - Simple revealed-as-you-explore map

### Deliverable
> Player explores 30 rooms across 6 regions, uses 10+ item types, solves 5+ puzzles, finds secrets, and reaches the final area.

---

## Phase 5 — Endgame (Week 9-10)

Goal: Final regions, boss, story completion.

### Milestones

1. **Blackfang Mountain & Forgotten Depths (10 rooms combined)**
   - Final tilesets (mines, dungeon)
   - Haunted Armour enemies
   - Puzzle chambers (3 relics to unlock shrine)
   - The Lost King NPC encounter

2. **Final boss**
   - Simple pattern-based encounter (dodge, expose weak point, repeat)

3. **Story cutscenes**
   - Intro sequence
   - Key story beats
   - Ending sequence + Crown of Endless Riches

4. **Victory screen**

### Deliverable
> Complete game is playable start to finish: village → woods → watchtower → marsh → mountain → depths → boss → ending.

---

## Phase 6 — Polish (Week 11-12)

Goal: Juice, audio, balancing, and bug fixing.

### Milestones

1. **Sprite replacements**
   - Replace all placeholders with proper pixel-art sprites
   - Player animations (idle, walk, jump, climb, push, pickup, celebrate, hurt)

2. **Audio**
   - Region themes (chiptune)
   - Sound effects (jump, pickup, door, secret, damage)

3. **Visual polish**
   - Screen shake on damage/explosions
   - Particle effects (dust, sparkle, leaves)
   - Smooth room transitions (slide, fade)

4. **Balancing & tuning**
   - Heart placement
   - Enemy speed/damage
   - Puzzle difficulty curve

5. **Save system completion**
   - Auto-save at checkpoints
   - Load game from title screen
   - Multiple save slots (optional)

### Deliverable
> Polished, shippable game.

---

## Room Data Format (Reference)

```json
{
  "id": "village_01",
  "name": "Village Square",
  "region": "goblin_village",
  "width": 24,
  "height": 14,
  "tile_size": 16,
  "layers": [
    {"name": "ground", "data": [[...]]},
    {"name": "decorations", "data": [[...]]}
  ],
  "collision": [[...]],
  "background": "village_bg.png",
  "music": "village_theme.ogg",
  "exits": [
    {"direction": "right", "target": "village_02", "x": 23, "y": 10},
    {"direction": "up", "target": "watchtower_01", "x": 12, "y": 0}
  ],
  "objects": [
    {"type": "item", "id": "rope", "x": 5, "y": 8},
    {"type": "npc", "id": "chief", "x": 10, "y": 6}
  ],
  "puzzles": [],
  "checkpoint": true
}
```

---

## Key Design Decisions

1. **Room size 384×216** at 16px tiles = 24×13.5 tiles; use 24×14 grid.
2. **Display at 2x scale** = 768×432 window, with fullscreen option.
3. **No physics engine** — custom AABB collision, simple gravity, no slopes initially.
4. **Data-driven everything** — rooms, items, NPCs, dialogue, puzzles all in JSON. No hardcoded content.
5. **Save format** JSON — inventory array, current room, puzzle states, health, position.
6. **Tile size 16×16** — classic look, easy to author.
7. **Screen-edge exits** — walking past the left/right/top/bottom edge triggers a room transition (classic Dizzy style).
8. **Player sprite 48×64** (3-4 tiles tall) or 64×64.

---

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Scope too large for solo dev | Phased delivery; each phase is playable; cut content if needed |
| Art asset creation bottleneck | Use placeholders until Phase 6; focus on gameplay first |
| Puzzle logic complexity | Simple condition-action system (JSON-driven) |
| Room count (30) manageable solo | Data-driven JSON; rapid iteration |
| Pygame performance at scale | `pygame-ce` render batching, dirty rects, sprite groups |

---

## Estimated Timeline (Solo Dev)

| Phase | Weeks | Hours |
|---|---|---|
| 1 — Foundation | 2 | 20-30 |
| 2 — Content Pipeline | 2 | 20-30 |
| 3 — Gameplay Systems | 2 | 20-30 |
| 4 — Content Expansion | 2 | 20-30 |
| 5 — Endgame | 2 | 15-25 |
| 6 — Polish | 2 | 20-30 |
| **Total** | **12 weeks** | **~115-175 hours** |
