import pyxel

pyxel.init(256, 256)
pyxel.load("my_resource.pyxres")  # データファイル読込

def update():
    global x
    x = (x + 10) % 256

def draw():
    global x
    pyxel.cls(0)
    pyxel.blt(x, 100, 0, 0, 0, 16, 16, 1)

x = 10
pyxel.run(update, draw)
