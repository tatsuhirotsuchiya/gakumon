import pyxel

pyxel.init(160, 120)
x = 0
Delta = 10


def update():
    global x
    x = (x + Delta) % 160


def draw():
    global x
    pyxel.cls(0)
    pyxel.rect(x, 10, x+10, 20, 11)

pyxel.run(update, draw)
