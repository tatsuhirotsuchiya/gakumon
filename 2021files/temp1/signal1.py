import pyxel

pyxel.init(160, 160)

# 画面の塗りつぶし
pyxel.cls(1)
# 長方形
pyxel.rect(5, 5, 120, 40, 13)
# 円
pyxel.circ(30, 25, 15, 11)
# 円
pyxel.circ(65, 25, 15, 10)
# 円
pyxel.circ(100, 25, 15, 8)

# 画面表示
pyxel.show()
