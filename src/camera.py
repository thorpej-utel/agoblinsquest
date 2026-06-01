class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.target_x = 0
        self.target_y = 0

    def reset(self):
        self.x = 0
        self.y = 0
        self.target_x = 0
        self.target_y = 0

    def set_target(self, x, y):
        self.target_x = x
        self.target_y = y

    def update(self, dt):
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        if abs(dx) < 1 and abs(dy) < 1:
            self.x = self.target_x
            self.y = self.target_y
            return True
        speed = 2000.0
        self.x += max(-speed * dt, min(speed * dt, dx))
        self.y += max(-speed * dt, min(speed * dt, dy))
        return False

    def apply(self, rect):
        return rect.move(-self.x, -self.y)
