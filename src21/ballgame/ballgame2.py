import pyxel
import random
import ballclass
import playerclass

pyxel.init(256, 256)
pyxel.load("my_resource.pyxres")

counter = 0
player = playerclass.Player()
balls = []
state = 'GAMEOVER'

for i in range(8):
    newball = ballclass.Ball(100, 0, \
        random.randint(-8, 8), random.randint(4, 8))
    balls.append(newball)

def update():
    global state
    if state == 'GAMEOVER':
        if pyxel.btn(pyxel.KEY_SPACE):
            state = 'PLAYING'
    else:
        update_playing()
        

def update_playing():
    global player, balls, counter, state
    player.update()
    for b in balls:
        b.update()

    counter = counter + 1

    for b in balls:
        if b.x - 20 < player.x < b.x + 20 and \
            b.y - 20 < player.y < b.y + 20:
            counter = 0
            pyxel.play(0, 0)
            state = 'GAMEOVER'


def draw():
    global player, balls, counter
    pyxel.cls(12)
    player.draw()
    for b in balls:
        b.draw()
    pyxel.text(5, 4, str(counter), 1)

pyxel.run(update, draw)
