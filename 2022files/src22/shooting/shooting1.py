import pyxel
import random
import initialization  # initialization.pyを読み込む
from ballclass import Ball  # ballclass を Ball.pyから読み込む
from playerclass import Player  # playerclassをPlayer.pyからを読み込む

pyxel.init(256, 256)
initialization.initialize()

counter = 0
player = Player()
balls = []
state = 'GAMEOVER'
hiscore = 0


def update():
    global state
    if state == 'GAMEOVER':
        if pyxel.btn(pyxel.KEY_SPACE):
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
    global player, balls, counter, state, hiscore
    player.update()
    for b in balls:
        b.update()

    counter = counter + 1

    for b in balls:
        if b.x - 10 < player.x < b.x + 10 and \
                b.y - 10 < player.y < b.y + 10:
            pyxel.play(0, 0)
            state = 'GAMEOVER'
            hiscore = max(counter, hiscore)


def draw():
    global player, balls, counter, hiscore
    pyxel.cls(12)
    player.draw()
    for b in balls:
        b.draw()
    pyxel.text(5, 4, str(counter), 1)
    pyxel.text(220, 4, str(hiscore), 1)
    if state == 'GAMEOVER':
        pyxel.text(100, 100, 'Game Over', 8)

pyxel.run(update, draw)
