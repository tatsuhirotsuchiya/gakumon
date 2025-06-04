import pyxel
import time  # ゲームのときは不要

pyxel.init(256, 256)
pyxel.load("my_resource.pyxres")  # データファイル読込

pyxel.play(2, 0)  # チャンネル2にSOUND 0を流す

# 1秒まつ．ゲームの時は不要．
# プログラムがすぐ終わって音がならないのを防ぐ
time.sleep(1)
