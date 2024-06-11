import pyxel


class Player:
    def __init__(self):
        self.x = 120
        self.y = 220

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = max(self.x - 4, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = min(self.x + 4, 240)
        if pyxel.btn(pyxel.KEY_UP):
            self.y = max(self.y - 4, 0)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y = min(self.y + 4, 240)

    def draw(self):
        # イメージバンク0の座標(0,0)から16x16ドットを取ってきて
        # プレーヤー（飛行機）として表示
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)


class Ball:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def update(self):
        self.x = (self.x + self.dx) % 256
        self.y = (self.y + self.dy) % 256

    def draw(self):
        pyxel.circ(self.x + 8, self.y + 8, 8, 4)


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
