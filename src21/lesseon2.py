import pyxel

pyxel.init(256, 256)

player = [80, 80]


def update():
    global player
    if pyxel.btn(pyxel.KEY_LEFT):
        player[0] = max(player[0] - 4, 0)
    if pyxel.btn(pyxel.KEY_RIGHT):
        player[0] = player[0] + 4
    if pyxel.btn(pyxel.KEY_DOWN):
        player[1] = max(player[1] - 4, 0)
    if pyxel.btn(pyxel.KEY_UP):
        player[1] = min(player[1] + 4, 256)


def draw():
    global player
    pyxel.cls(12)
    pyxel.circ(player[0], player[1], 10, 2)

pyxel.run(update, draw)
