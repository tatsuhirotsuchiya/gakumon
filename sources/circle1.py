import pyxel
import random

pyxel.init(160, 160)

# 画面の塗りつぶし
pyxel.cls(1)

for radius in range(10, 30, 10):
    color_rand = random.randint(0, 15)
    pyxel.circb(80, 80, radius, color_rand)

# 画面表示
pyxel.show()
