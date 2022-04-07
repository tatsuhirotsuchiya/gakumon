import pyxel

pyxel.init(256, 256)

pyxel.load("my_resource.pyxres")


class Ball:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def update(self):
        self.x = (self.x + self.dx) % 256
        self.y = (self.y + self.dy) % 256

    def draw(self):
        pyxel.circ(self.x, self.y, 10, 4)

player = [80, 80]
ball = Ball(0, 0, 5, 7)
ball2 = Ball(200, 0, -6, 4)  # 2個目のボール
counter = 0
highscore = 0  # ハイスコア

state = 'GAMEOVER'

def update():
    global counter, highscore, state
    if state == 'GAMEOVER':
        if pyxel.btn(pyxel.KEY_SPACE):
            state = 'PLAYING'
    else:
        update_player()
        update_ball()
        detect_collision()
        highscore = max(counter, highscore)  # ハイスコア更新


def update_player():
    global player
    if pyxel.btn(pyxel.KEY_LEFT):
        player[0] = max(player[0] - 4, 0)
    if pyxel.btn(pyxel.KEY_RIGHT):
        player[0] = min(player[0] + 4, 256)
    if pyxel.btn(pyxel.KEY_UP):
        player[1] = max(player[1] - 4, 0)
    if pyxel.btn(pyxel.KEY_DOWN):
        player[1] = min(player[1] + 4, 256)


def update_ball():
    global ball, ball2
    ball.update()
    ball2.update()  # 2個目のボール


def detect_collision():
    global player, ball, ball2, counter, state
    # 長い文を \ で折り返して，複数行に記述
    if ball.x - 20 < player[0] < ball.x + 20 and \
            ball.y - 20 < player[1] < ball.y + 20:
        counter = 0
        state = 'GAMEOVER'
    elif ball2.x - 20 < player[0] < ball2.x + 20 and \
            ball2.y - 20 < player[1] < ball2.y + 20:  # 2個目のボール
        counter = 0
        state = 'GAMEOVER'
    else:
        counter = counter + 1


def draw():
    global player, ball, ball2, counter, highscore
    pyxel.cls(12)
    # pyxel.circ(player[0], player[1], 10, 2) # 自分のキャラ
    pyxel.blt(player[0], player[1], 0, 0, 0, 16, 16, 0)
    
    ball.draw()
    ball2.draw()
    pyxel.text(5, 4, str(counter), 1)
    pyxel.text(220, 4, str(highscore), 1)  # ハイスコア表示

pyxel.run(update, draw)
