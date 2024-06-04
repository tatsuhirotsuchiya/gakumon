import pyxel
pyxel.init(256, 256)


class Player:
    def __init__(self):
        self.y = 150  # y座標
        self.dy = 0   # ジャンプ/落下のスピード

    def update(self):
        self.y = min(150, self.y + self.dy)
        self.dy = min(self.dy + 1, 8)
        if self.y == 150 and pyxel.btnp(pyxel.KEY_SPACE):
            self.dy = -5

    def draw(self):
        pyxel.rectb(200, self.y, 16, 16, 15)


player = Player()


def update():
    player.update()


def draw():
    pyxel.cls(0)
    player.draw()


pyxel.run(update, draw)
