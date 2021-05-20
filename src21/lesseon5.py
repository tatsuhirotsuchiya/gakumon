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

player = [80, 80]
ball = Ball(0, 0, 5, 7)
ball2 = Ball(0, 250, -10, 5)
counter = 0

def update():
    update_player()
    update_ball()
    check_()

def update_player():
    global player
    if pyxel.btn(pyxel.KEY_LEFT):
        player[0] = max(player[0] - 4, 0)
    if pyxel.btn(pyxel.KEY_RIGHT):
        player[0] = min(player[0] + 4, 256)
    if pyxel.btn(pyxel.KEY_UP):
        player[1] = max(player[1] - 4, 0)
    if pyxel.btn(pyxel.KEY_DOWN):
        player[1] = min(player[1] + 4, 256)

def update_ball():
    global ball, ball2
    ball.update()
    ball2.update()

def check_():
    global player, ball, ball2, counter
    if ball.x - 10 < player[0] < ball.x + 10 and ball.y - 10 < player[1] < ball.y + 10:
        counter = 0
    else:
        counter = counter + 1


def draw():
    global player, ball, counter
    pyxel.cls(12)
    pyxel.circ(player[0], player[1], 10, 2)
    ball.draw()
    # ball2.draw()
    pyxel.text(5, 4, str(counter), 1)

pyxel.run(update, draw)
