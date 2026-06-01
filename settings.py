# Constants
TILE_SIZE = 16
ROOM_COLS = 24
ROOM_ROWS = 14
INTERNAL_WIDTH = ROOM_COLS * TILE_SIZE   # 384
INTERNAL_HEIGHT = ROOM_ROWS * TILE_SIZE  # 224
WINDOW_WIDTH = INTERNAL_WIDTH * 2        # 768
WINDOW_HEIGHT = INTERNAL_HEIGHT * 2      # 448
FPS = 60

# Physics
GRAVITY = 800.0
PLAYER_SPEED = 150.0
JUMP_VELOCITY = -320.0
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 32

# Paths
DATA_DIR = "data"
ROOMS_DIR = f"{DATA_DIR}/rooms"
ASSETS_DIR = "assets"
SAVES_DIR = "saves"

# Tile colors (RGB)
TILE_COLORS = {
    0: None,
    1: (101, 67, 33),     # dirt
    2: (85, 139, 47),     # grass
    3: (120, 120, 120),   # stone
    4: (60, 40, 20),      # wood platform
    5: (180, 130, 40),    # sandy ground
}
