import pyxel
import random

pyxel.init(160, 160)

# 画面の塗りつぶし 
pyxel.cls(1)

for y in range(0, 161, 20):
    for x in range(0, 161, 20):
        color_rand = random.randint(0, 15)
        pyxel.circ(x, y, 9, color_rand)

# 画面表示
pyxel.show()