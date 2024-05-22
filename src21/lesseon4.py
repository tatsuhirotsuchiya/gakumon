import pyxel

pyxel.init(256, 256)


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
        pyxel.circ(self.x, self.y, 10, 4)


player_x = 80
player_y = 80
ball = Ball(0, 0, 5, 7)


def update():
    update_player()
    update_ball()


def update_player():
    global player_x, player_y
    if pyxel.btn(pyxel.KEY_LEFT):
        player_x = max(player_x - 4, 0)
    if pyxel.btn(pyxel.KEY_RIGHT):
        player_x = player_x + 4
    if pyxel.btn(pyxel.KEY_DOWN):
        player_y = max(player_y - 4, 0)
    if pyxel.btn(pyxel.KEY_UP):
        player_y = min(player_y + 4, 256)


def update_ball():
    ball.update()


def draw():
    pyxel.cls(12)
    pyxel.circ(player_x, player_y, 10, 2)
    ball.draw()


pyxel.run(update, draw)
