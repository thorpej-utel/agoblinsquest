# A Goblin's Quest — Task List

## Phase 1 — Foundation

- [ ] P1.1 Create virtual environment, install `pygame-ce`
- [ ] P1.2 Scaffold `main.py` with game loop template
- [ ] P1.3 Create `settings.py` (screen size, FPS, asset paths, constants)
- [ ] P1.4 Build `engine.py` state machine (TITLE, PLAYING, PAUSED, etc.)
- [ ] P1.5 Build `input.py` input handler (key mapping, press/release)
- [ ] P1.6 Build `camera.py` world-to-screen coordinate transform
- [ ] P1.7 Build `rooms/tilemap.py` tile renderer
- [ ] P1.8 Build `rooms/room.py` room data loading & collision grid
- [ ] P1.9 Build `entities/player.py` player movement (left/right/jump)
- [ ] P1.10 Build `systems/physics.py` gravity & AABB collision
- [ ] P1.11 Implement screen-edge room transitions
- [ ] P1.12 Create 2 placeholder JSON rooms (village_01, village_02)

## Phase 2 — Content Pipeline

- [ ] P2.1 Create JSON schemas for rooms, items, NPCs, dialogue
- [ ] P2.2 Build `rooms/manager.py` room loading, caching, transitions
- [ ] P2.3 Create placeholder JSON rooms (village 4-6 room starter set)
- [ ] P2.4 Build `systems/inventory.py` item grid & management (max 6)
- [ ] P2.5 Create `data/items.json` with initial item definitions
- [ ] P2.6 Implement in-world item pickups
- [ ] P2.7 Build `ui/menus.py` inventory screen overlay
- [ ] P2.8 Build `entities/npc.py` NPC rendering & interaction zones
- [ ] P2.9 Build `systems/dialogue.py` typewriter text system
- [ ] P2.10 Build `ui/dialogue_box.py` dialogue box rendering
- [ ] P2.11 Create `data/npcs.json` NPC definitions
- [ ] P2.12 Create `data/dialogues.json` dialogue trees
- [ ] P2.13 Build `ui/hud.py` hearts, item slots, gold tooth counter

## Phase 3 — Gameplay Systems

- [ ] P3.1 Build `systems/puzzle.py` condition-action engine
- [ ] P3.2 Create `data/puzzles.json` puzzle definitions
- [ ] P3.3 Implement triggerable objects (levers, doors, bridges)
- [ ] P3.4 Build `entities/enemy.py` base enemy + AI behaviours
- [ ] P3.5 Create `data/enemies.json` enemy definitions
- [ ] P3.6 Implement bat enemy (flying patrol)
- [ ] P3.7 Implement spider enemy (ground patrol)
- [ ] P3.8 Implement angry troll enemy (path blocker)
- [ ] P3.9 Implement contact damage & invulnerability frames
- [ ] P3.10 Implement health system (4 hearts, food restore)
- [ ] P3.11 Implement death & respawn at last checkpoint
- [ ] P3.12 Build `systems/save.py` JSON serialization
- [ ] P3.13 Implement auto-save on checkpoint rooms
- [ ] P3.14 Implement hazards (spikes, toxic pools)
- [ ] P3.15 Implement moving platforms

## Phase 4 — Content Expansion

### Rooms
- [ ] P4.1 Design Goblin Village (5 rooms: square, huts, market, shaman, blacksmith)
- [ ] P4.2 Design Mushroom Woods (5 rooms: entrance, caves, spider nest, hidden path, clearing)
- [ ] P4.3 Design Old Watchtower (3 rooms: base, mid, top)
- [ ] P4.4 Design Troll Marsh (5 rooms: entrance, pools, troll camp, ruins, deep marsh)
- [ ] P4.5 Design Blackfang Mountain (6 rooms: entrance, mines, ruins, puzzle chamber, nest, summit)
- [ ] P4.6 Design Forgotten Depths (4 rooms: entrance, king's chamber, treasury, boss room)
- [ ] P4.7 Design transitional caves (2 rooms: village→woods, marsh→mountain)
- [ ] P4.8 Create tilesets for each region

### Items & Puzzles
- [ ] P4.9 Implement full item set (~20 items: Rope, Torch, Mushroom, Key, Hammer, Gear, Gemstone, Golden Acorn, Crystal Lens, Ancient Coin, Wooden Plank, Hook, Apple, Roasted Mushroom, Honey Cake, etc.)
- [ ] P4.10 Implement Broken Bridge puzzle (Rope + Plank)
- [ ] P4.11 Implement Hungry Troll puzzle (Mushroom → Key)
- [ ] P4.12 Implement Broken Lift puzzle (Gear + Hammer)
- [ ] P4.13 Implement Dark Cave puzzle (Torch reveals path)
- [ ] P4.14 Implement Locked Shrine puzzle (3 relics → progression)
- [ ] P4.15 Place Gold Teeth collectibles across all regions (~30)
- [ ] P4.16 Add secret rooms & passages

### Optional
- [ ] P4.17 Build map screen system

## Phase 5 — Endgame

- [ ] P5.1 Implement final boss encounter (pattern-based)
- [ ] P5.2 Build intro cutscene
- [ ] P5.3 Build story beat cutscenes
- [ ] P5.4 Build ending cutscene + Crown of Endless Riches
- [ ] P5.5 Build victory screen
- [ ] P5.6 Implement The Lost King NPC encounter
- [ ] P5.7 Full playthrough test & fix progression blockers

## Phase 6 — Polish

- [ ] P6.1 Create proper player sprite (48x64 or 64x64 with all animations)
- [ ] P6.2 Create NPC sprites (Goblin Chief, Merchant Gorb, Professor Squig, Bog Witch, Lost King)
- [ ] P6.3 Create enemy sprites (bat, spider, troll, haunted armour, fire beetle)
- [ ] P6.4 Add region background art
- [ ] P6.5 Add region music themes (chiptune)
- [ ] P6.6 Add sound effects (jump, pickup, door, secret, damage, coin)
- [ ] P6.7 Add screen shake on damage
- [ ] P6.8 Add particle effects (dust, sparkle, leaves)
- [ ] P6.9 Add smooth room transitions (slide/fade)
- [ ] P6.10 Balance heart placement, enemy speed, puzzle difficulty
- [ ] P6.11 Complete save/load from title screen
- [ ] P6.12 Final bug-fixing pass
