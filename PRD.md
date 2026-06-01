# A Goblin's Quest

## Game Design Document (GDD)

Version 1.0

---

# Overview

**A Goblin's Quest** is a room-to-room fantasy adventure platform game inspired by classic Codemasters Dizzy titles and other late-80s/early-90s home computer adventures.

Players control **Grub**, a young goblin who dreams of becoming a legendary adventurer despite being considered useless by his tribe.

The game combines exploration, item collection, environmental puzzles, NPC interaction, and light platforming across a large interconnected world.

The goal is to create a game that feels like:

> A lost 1991 Codemasters game recreated with modern pixel art.

---

# Design Goals

## Inspirations

* Magicland Dizzy
* Fantasy World Dizzy
* Treasure Island Dizzy
* Seymour Goes to Hollywood
* Wonder Boy
* Monty Mole

## Modern Enhancements

* Large detailed pixel-art sprites
* Smooth room-to-room scrolling
* Improved visual storytelling
* Auto-save system
* Optional map system
* Expressive NPC animations

## Core Philosophy

Simple controls, memorable characters, exploration-driven gameplay, and puzzles that reward curiosity.

---

# Story

The Goblin King has disappeared.

The tribal shamans believe he ventured beneath Blackfang Mountain searching for the mythical **Crown of Endless Riches**.

When the tribe's greatest warriors fail to return, a young maintenance goblin named **Grub** accidentally becomes the kingdom's last hope.

Armed with little more than determination and questionable common sense, Grub begins:

# A Goblin's Quest

---

# Main Character

## Grub

### Personality

* Optimistic
* Curious
* Slightly cowardly
* Frequently gets into trouble

### Appearance

* Green skin
* Large ears
* Patchwork tunic
* Small satchel
* Bare feet

### Sprite Size

Recommended:

* 48x64 pixels

or

* 64x64 pixels

The character should feel significantly larger and more detailed than classic 8-bit adventure sprites.

---

# Gameplay Loop

1. Explore new rooms
2. Discover items
3. Meet NPCs
4. Solve puzzles
5. Unlock new areas
6. Find secrets
7. Advance the story
8. Reach the final dungeon

---

# World Structure

## Goblin Village

Starting area.

Features:

* Goblin huts
* Market
* Blacksmith
* Shaman hut
* Training area

Purpose:

* Tutorials
* Story introduction
* Basic item trading

---

## Mushroom Woods

A dense forest of giant mushrooms.

Features:

* Hidden caves
* Friendly insects
* Dangerous spiders
* Secret paths

---

## Old Watchtower

A vertical platforming region.

Features:

* Ladders
* Collapsing floors
* Treasure rooms
* Shortcut routes

---

## Troll Marsh

A hazardous swamp.

Features:

* Toxic pools
* Moving platforms
* Hidden relics
* Troll settlements

---

## Blackfang Mountain

The primary late-game region.

Features:

* Mines
* Ancient ruins
* Monster nests
* Puzzle chambers

---

## Forgotten Depths

Final game area.

Features:

* Lost king
* Ancient treasure
* Final boss encounter
* Crown of Endless Riches

---

# Room System

Classic room-based adventure design.

Room size recommendation:

* 320x180
* 384x216

Connections:

* Left
* Right
* Up
* Down

Crossing a screen edge transitions to a connected room.

No open-world streaming.

This preserves the classic adventure-game feel.

---

# Inventory System

Inventory size:

* Maximum 6 items

The player must manage inventory carefully.

### Example Items

* Rope
* Torch
* Mushroom
* Key
* Hammer
* Gemstone
* Broken Gear
* Golden Acorn
* Crystal Lens
* Ancient Coin

Inventory management is part of puzzle solving.

---

# Example Puzzles

## Broken Bridge

Requirements:

* Rope
* Wooden Plank

Result:

* Access to new region

---

## Hungry Troll

Requirements:

* Giant Mushroom

Result:

* Troll gives player a key

---

## Broken Lift

Requirements:

* Gear
* Hammer

Result:

* Access to deeper mines

---

## Dark Cave

Requirements:

* Torch

Result:

* Hidden paths become visible

---

## Locked Shrine

Requirements:

* Three ancient relics

Result:

* Story progression

---

# NPCs

## Goblin Chief

Provides objectives and story updates.

---

## Merchant Gorb

Trades rare items.

---

## Professor Squig

Inventor and gadget maker.

---

## Bog Witch

Offers magical assistance.

Usually requires unusual ingredients.

---

## The Lost King

Central story character.

---

# Enemies

Combat is not the primary focus.

Enemies function mainly as hazards and obstacles.

## Cave Bats

Simple flying enemies.

---

## Giant Spiders

Ground patrol hazards.

---

## Angry Trolls

Block pathways.

---

## Haunted Armour

Dungeon guardians.

---

## Fire Beetles

Fast-moving environmental hazards.

---

# Health System

Simple heart-based system.

Starting health:

♥ ♥ ♥ ♥

Damage removes hearts.

Food restores health.

Examples:

* Apple
* Roasted Mushroom
* Honey Cake

---

# Collectibles

## Gold Teeth

Primary collectible.

Used for:

* Trading
* Unlockables
* Completion percentage

Hidden throughout the world.

---

# Secrets

Each region contains:

* Hidden rooms
* Secret passages
* Joke items
* Developer references
* Bonus treasure

Target:

100+ discoverable secrets.

---

# Art Direction

## Style

Modern pixel art inspired by:

* SNES
* Amiga
* Late-era C64 cover art

### Colour Palette

* Rich greens
* Warm browns
* Gold highlights
* Purple shadows
* Torch-lit environments

### Animation

Grub should have animations for:

* Idle
* Walk
* Run
* Jump
* Climb
* Push
* Pick up item
* Celebrate
* Hurt

---

# Audio

## Music

Fantasy chiptune soundtrack inspired by classic SID compositions.

Each major region should have its own theme.

## Sound Effects

* Jump
* Coin pickup
* Item pickup
* Door opening
* Lever activation
* Goblin grunts
* Secret discovered

---

# Progression

Players gain access to new regions by:

* Solving puzzles
* Finding items
* Helping NPCs
* Unlocking shortcuts

The world gradually opens up as knowledge and inventory expand.

---

# Estimated Scope

## Rooms

120–150

## NPCs

20–30

## Puzzle Items

50+

## Secrets

100+

## Gameplay Length

Main Story:
4–8 hours

Completionist:
10+ hours

---

# Elevator Pitch

*A Goblin's Quest* is a charming room-to-room fantasy adventure inspired by the classic Dizzy games. Explore a vast interconnected world, solve puzzles, collect items, uncover secrets, and discover the fate of the missing Goblin King in a modern pixel-art love letter to the golden age of home-computer gaming.
