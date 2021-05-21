import pyxel

pyxel.init(256, 256)

player = [80, 80]
ball = [0, 0, 5, 7]


def update():
    update_player()
    update_ball()


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
    global ball
    ball[0] = (ball[0] + ball[2]) % 256
    ball[1] = (ball[1] + ball[3]) % 256


def draw():
    global player, ball
    pyxel.cls(12)
    pyxel.circ(player[0], player[1], 10, 2)
    pyxel.circ(ball[0], ball[1], 10, 4)

pyxel.run(update, draw)
