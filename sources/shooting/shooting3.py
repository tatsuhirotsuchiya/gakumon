import pyxel
import random
from classes import Ball  # ballclass を classes.py から読み込む
from classes import Player  # playerclass を classes.py からを読み込む
from classes import Missile  # Missile を classes.py からを読み込む

pyxel.init(256, 256)

# 飛行機のイメージ
pyxel.images[0].set(
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
        "00cc00888800cc00"])

# サウンド
pyxel.sounds[0].set("a3a2c1a1", "p", "7", "s", 5)
pyxel.sounds[1].set("a3a2c2c2", "n", "7742", "s", 5)

# 変数
counter = 0
player = Player()
balls = []
hiscore = 0
missiles = []


def start_game():
    global counter, balls, player, missiles
    counter = 0
    player = Player()
    balls = []
    for i in range(8):
        newball = Ball(100, 0,
                       random.randint(-8, 8), random.randint(4, 8))
        balls.append(newball)
    missiles = []


def update():
    global counter, hiscore, missiles
    counter = counter + 1
    player.update()
    for b in balls:
        b.update()
    for b in balls:
        if b.x - 10 < player.x < b.x + 10 and \
                b.y - 10 < player.y < b.y + 10:
            pyxel.play(0, 0)
            hiscore = max(counter, hiscore)
            start_game()
    # スペースキーが押されたら，ミサイルをリストmissilesに追加し，音を出す
    if pyxel.btnp(pyxel.KEY_SPACE):
        missiles.append(Missile(player.x, player.y))
        pyxel.play(0, 0)
    # ボールとミサイルの当たり判定
    for b in balls:
        for m in missiles:
            if b.x - 10 < m.x < b.x + 10 and \
               b.y - 10 < m.y < b.y + 10:
                m.dead = True
                b.y = -10
    # 画面から消えていないミサイルだけnew_missilesにいれ，新しいmissilesとする
    new_missiles = []
    for m in missiles:
        m.update()
        if m.dead is False:
            new_missiles.append(m)
    missiles = new_missiles


def draw():
    pyxel.cls(12)
    player.draw()
    for b in balls:
        b.draw()
    pyxel.text(5, 4, str(counter), 1)
    pyxel.text(220, 4, str(hiscore), 1)
    for m in missiles:
        m.draw()


start_game()
pyxel.run(update, draw)
