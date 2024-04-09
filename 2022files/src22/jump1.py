import pyxel
pyxel.init(256, 256)


class Player:
    def __init__(self):
        self.y = 150
        self.vy = 0

    def update(self):
        self.y = min(150, self.y + self.vy)
        self.vy = min(self.vy + 1, 8)
        if self.y == 150 and pyxel.btnp(pyxel.KEY_SPACE):
            self.vy = -5

    def draw(self):
        pyxel.rectb(200, self.y, 16, 16, 15)

player = Player()


def update():
    player.update()


def draw():
    pyxel.cls(0)
    player.draw()

pyxel.run(update, draw)
