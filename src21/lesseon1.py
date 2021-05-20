import pyxel

pyxel.init(256, 256)

player_x = 80

def update():
    global player_x
    if pyxel.btn(pyxel.KEY_LEFT):
        player_x = max(player_x - 4, 0)
    if pyxel.btn(pyxel.KEY_RIGHT):
        player_x = player_x + 4

def draw():
    global player_x
    pyxel.cls(12)
    pyxel.circ(player_x, 100, 10, 2)

pyxel.run(update, draw)
