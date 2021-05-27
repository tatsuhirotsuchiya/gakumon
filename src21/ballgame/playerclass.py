import pyxel

class Player:
    def __init__(self):
        self.x = 120
        self.y = 120

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = max(self.x - 4, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = min(self.x + 4, 256)
        if pyxel.btn(pyxel.KEY_UP):
            self.y = max(self.y - 4, 0)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y = min(self.y + 4, 256)

    def draw(self):
        pyxel.circ(self.x, self.y, 10, 2)
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)
