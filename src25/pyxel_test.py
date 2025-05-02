import pyxel

pyxel.init(256, 256)


def update():
    pass


def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 12)


pyxel.run(update, draw)
