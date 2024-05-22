import pyxel

pyxel.init(256, 256)

player_x = 80
player_y = 80


def update():
    global player_x, player_y
    if pyxel.btn(pyxel.KEY_LEFT):
        player_x = max(player_x - 4, 0)
    if pyxel.btn(pyxel.KEY_RIGHT):
        player_x = player_x + 4
    if pyxel.btn(pyxel.KEY_DOWN):
        player_y = max(player_y - 4, 0)
    if pyxel.btn(pyxel.KEY_UP):
        player_y = min(player_y + 4, 256)


def draw():
    pyxel.cls(12)
    pyxel.circ(player_x, player_y, 10, 2)


pyxel.run(update, draw)
