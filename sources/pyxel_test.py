import pyxel

pyxel.init(160, 120)


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 12)


pyxel.run(update, draw)
