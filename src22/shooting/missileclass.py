import pyxel


class Missile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dead = False

    def update(self):
        self.y -= 16
        if self.y < 0:
            self.is_dead = True

    def draw(self):
        pyxel.rect(self.x, self.y, 2, 16, 8)
        pyxel.rect(self.x + 14, self.y, 2, 16, 8)
