import pyxel

def initialize():
    # グラフィックス
    # イメージバンク0に16x16のイメージを書き込む．座標0,0を左上とする．
    pyxel.image(0).set(
    0,
    0,
    [
    "0000cc8888cc0000",
    "0000cc8888cc0000",
    "0000cc777777cc00",
    "0000cc777777cc00",
    "0000cc77888877c0",
    "0000cc77888877c0",
    "cccc778833bb877c",
    "cccc778833bb077c",
    "7777778333387777",
    "7777778333387777",
    "778855cccc558877",
    "778855cccc558877",
    "8855cc7777cc5588",
    "8855cc7777cc5588",
    "00cc00888800cc00",
    "00cc00888800cc00"
     ])
    
    # サウンド
    pyxel.sound(0).set("a3a2c1a1", "p", "7", "s", 5)
    pyxel.sound(1).set("a3a2c2c2", "n", "7742", "s", 5)