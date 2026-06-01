import pygame
from settings import TILE_SIZE, ROOM_COLS, ROOM_ROWS

def move_and_collide(rect, vx, vy, dt, collision_map):
    rect.x += int(round(vx * dt))
    collided_x = _resolve_x(rect, vx, collision_map)
    if collided_x:
        vx = 0.0

    rect.y += int(round(vy * dt))
    grounded, collided_y = _resolve_y(rect, vy, collision_map)
    if collided_y:
        vy = 0.0

    return vx, vy, grounded


def _resolve_x(rect, vx, collision_map):
    left = rect.left // TILE_SIZE
    right = (rect.right - 1) // TILE_SIZE
    top = rect.top // TILE_SIZE
    bottom = (rect.bottom - 1) // TILE_SIZE
    collided = False

    for row in range(max(0, top), min(ROOM_ROWS, bottom + 1)):
        for col in range(max(0, left), min(ROOM_COLS, right + 1)):
            if not _is_solid(collision_map, row, col):
                continue
            tile_left = col * TILE_SIZE
            tile_right = tile_left + TILE_SIZE
            if rect.right > tile_left and rect.left < tile_right:
                collided = True
                if vx > 0:
                    rect.right = tile_left
                elif vx < 0:
                    rect.left = tile_right
                else:
                    if rect.left <= tile_left + TILE_SIZE // 2:
                        rect.left = tile_right
                    else:
                        rect.right = tile_left
    return collided


def _resolve_y(rect, vy, collision_map):
    left = rect.left // TILE_SIZE
    right = (rect.right - 1) // TILE_SIZE
    top = rect.top // TILE_SIZE
    bottom = (rect.bottom - 1) // TILE_SIZE
    grounded = False
    collided = False

    for row in range(max(0, top), min(ROOM_ROWS, bottom + 1)):
        for col in range(max(0, left), min(ROOM_COLS, right + 1)):
            if not _is_solid(collision_map, row, col):
                continue
            tile_top = row * TILE_SIZE
            tile_bottom = tile_top + TILE_SIZE
            if rect.bottom > tile_top and rect.top < tile_bottom:
                collided = True
                if vy >= 0:
                    rect.bottom = tile_top
                    grounded = True
                else:
                    rect.top = tile_bottom
    return grounded, collided


def _is_solid(collision_map, row, col):
    if row < 0 or row >= ROOM_ROWS or col < 0 or col >= ROOM_COLS:
        return False
    return collision_map[row][col] > 0

def is_on_ground(rect, collision_map):
    left = rect.left // TILE_SIZE
    right = (rect.right - 1) // TILE_SIZE
    if rect.bottom % TILE_SIZE == 0:
        bottom_tile = rect.bottom // TILE_SIZE
        if bottom_tile < ROOM_ROWS:
            for col in range(max(0, left), min(ROOM_COLS, right + 1)):
                if collision_map[bottom_tile][col] > 0:
                    return True
    return False
