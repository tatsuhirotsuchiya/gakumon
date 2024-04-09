import pyxel
import random
import initialization
from ballclass import Ball
from playerclass import Player
from missileclass import Missile

pyxel.init(256, 256)
initialization.initialize()

counter = 0
player = Player()
balls = []
state = 'GAMEOVER'
hiscore = 0
missiles = []


def update():
    global state
    if state == 'GAMEOVER':
        if pyxel.btn(pyxel.KEY_RETURN):
            start_game()
            state = 'PLAYING'
    else:
        update_playing()


def start_game():
    global counter, balls, player
    counter = 0
    player.x = 120
    player.y = 220
    new_balls = []
    for i in range(8):
        newball = Ball(100, 0,
                       random.randint(-8, 8), random.randint(4, 8))
        new_balls.append(newball)
    balls = new_balls


def update_playing():
    global player, balls, counter, state, hiscore, missiles
    player.update()

    for b in balls:
        b.update()

    counter = counter + 1

    for b in balls:
        if b.x - 10 < player.x < b.x + 10 and \
                b.y - 10 < player.y < b.y + 10:
            pyxel.play(0, 1)
            state = 'GAMEOVER'
            hiscore = max(counter, hiscore)

    if pyxel.btnp(pyxel.KEY_SPACE):
        missiles.append(Missile(player.x, player.y))
        pyxel.play(0, 0)
    for m in missiles:
        m.update()

    # ボールとミサイルの当たり判定
    for b in balls:
        for m in missiles:
            if b.x - 10 < m.x < b.x + 10 and \
               b.y - 10 < m.y < b.y + 10:
                m.dead = True
                b.y = -10

    new_missiles = []
    for m in missiles:
        if m.dead is False:
            new_missiles.append(m)
    missiles = new_missiles


def draw():
    global player, balls, counter, hiscore, missiles
    pyxel.cls(12)
    player.draw()
    for b in balls:
        b.draw()
    pyxel.text(5, 4, str(counter), 1)
    pyxel.text(220, 4, str(hiscore), 1)
    if state == 'GAMEOVER':
        pyxel.text(100, 100, 'Game Over', 8)
    for m in missiles:
        m.draw()

pyxel.run(update, draw)
