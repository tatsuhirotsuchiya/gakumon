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

# 変数の準備
player = None
ball = None
ball2 = None
gamestarted = False

def initialize():
    global player, ball, ball2
    player = [80, 80]
    ball = Ball(0, 0, 5, 7)
    ball2 = Ball(200, 0, -8, 4)

def update():
    global gamestarted
    if gamestarted == False:
        if pyxel.btn(pyxel.KEY_SPACE):
            initialize()
            gamestarted = True
    else:
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
    global player, ball, ball2
    if (player[0] )

def draw():
    global player, ball
    pyxel.cls(12)
    pyxel.circ(player[0], player[1], 10, 2)
    ball.draw()
    ball2.draw()


initialize()
pyxel.run(update, draw)
