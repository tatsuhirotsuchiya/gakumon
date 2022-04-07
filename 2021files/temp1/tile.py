import pyxel
import random

pyxel.init(160, 160)

# 画面の塗りつぶし
pyxel.cls(1)

for y in range(0, 161, 20):
    for x in range(0, 161, 20):
        pyxel.circ(x, y, 10, 15)
        # ここに処理を追加して
        # 課題を完成させる

# 画面表示
pyxel.show()

