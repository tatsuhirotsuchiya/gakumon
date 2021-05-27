import pyxel

class Player:
    def __init__(self):
        self.x = 120
        self.y = 120

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = max(player[0] - 4, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = min(player[0] + 4, 256)
        if pyxel.btn(pyxel.KEY_UP):
            self.y = max(player[1] - 4, 0)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y = min(player[1] + 4, 256)

    def draw(self):
        pyxel.circ(self.x, self.y, 10, 2)
