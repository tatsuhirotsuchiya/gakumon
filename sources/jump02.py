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


class Can:
    def __init__(self, x, dx):
        self.x = x
        self.dx = dx

    def update(self):
        self.x = self.x + self.dx
        if self.x > 256:  # 左端に到達したら右端に移動
            self.x = -20

    def draw(self):
        pyxel.rectb(self.x, 150, 16, 16, 12)


class Block:
    def __init__(self, x, col):
        self.x = x
        self.col = col

    def update(self):
        self.x = self.x + 4
        if self.x >= 256:
            self.x = -64

    def draw(self):
        pyxel.rectb(self.x, 166, 64, 16, self.col)


player = Player()
cans = [Can(-100, 5), Can(-250, 8)]  # カンのリスト
life = 0
blocks = [Block(0, 1), Block(64, 2), Block(128, 1),
          Block(192, 2), Block(-64, 1)]  # ブロックのリスト


def update():
    global life
    if life <= 0:
        if pyxel.btnp(pyxel.KEY_SPACE):
            life = 20
    else:
        player.update()
        for can in cans:
            can.update()
            if can.x - 10 < 200 < can.x + 10 and \
                    140 <= player.y <= 150:  # あたり判定
                life = life - 1
                break
        for block in blocks:
            block.update()


def draw():
    pyxel.cls(0)
    player.draw()
    for can in cans:
        can.draw()
    pyxel.text(0, 0, str(life), 10)
    for block in blocks:
        block.draw()


pyxel.run(update, draw)
