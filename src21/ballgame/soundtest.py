import pyxel
import random

pyxel.init(256, 256)
pyxel.load("my_resource.pyxres")  # データファイル読込

pyxel.play(2, 0) # チャンネル2にSOUND 0を流す
