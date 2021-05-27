import pyxel
import random
import ballclass

pyxel.init(256, 256)

'''
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
'''


player = [80, 80]
counter = 0
balls = []
for i in range(10):
    # balls.append(Ball(120, 0, random.randint(4, 8), random.randint(4, 8)))
    balls.append(ballclass.Ball(100, 0, random.randint(-8, 8), random.randint(4, 8)))

def update():
    update_player()
    update_ball()
    detect_collision()


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
    global balls
    for b in balls:
        b.update()


def detect_collision():
    global player, balls, counter
    counter = counter + 1
    # 長い文を \ で折り返して，複数行に記述
    for b in balls:
        if b.x - 20 < player[0] < b.x + 20 and \
            b.y - 20 < player[1] < b.y + 20:
            counter = 0


def draw():
    global player, ball, counter
    pyxel.cls(12)
    pyxel.circ(player[0], player[1], 10, 2)
    for b in balls:
        b.draw()
    pyxel.text(5, 4, str(counter), 1)

pyxel.run(update, draw)
