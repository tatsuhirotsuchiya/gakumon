import pyxel

pyxel.init(256, 256)

player_x = 80
player_y = 80
ball_x = 0
ball_y = 0
ball_sx = 5
ball_sy = 7


def update():
    update_player()
    update_ball()


def update_player():
    global player_x, player_y
    if pyxel.btn(pyxel.KEY_LEFT):
        player_x = max(player_x - 4, 0)
    if pyxel.btn(pyxel.KEY_RIGHT):
        player_x = player_x + 4
    if pyxel.btn(pyxel.KEY_DOWN):
        player_y = max(player_y - 4, 0)
    if pyxel.btn(pyxel.KEY_UP):
        player_y = min(player_y + 4, 256)


def update_ball():
    global ball_x, ball_y
    ball_x = (ball_x + ball_sx) % 256
    ball_y = (ball_y + ball_sy) % 256


def draw():
    pyxel.cls(12)
    pyxel.circ(player_x, player_y, 10, 2)
    pyxel.circ(ball_x, ball_y, 10, 4)


pyxel.run(update, draw)
