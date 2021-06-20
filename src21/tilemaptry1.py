import pyxel
pyxel.init(128, 128)

# グラフィックス
# イメージバンク0に8x16のイメージを書き込む．座標0,0を左上とする．
pyxel.image(0).set(
    0,
    0,
    [
        "44444444",  # 壁
        "42222444",
        "44422244",
        "44222444",
        "42224424",
        "22244444",
        "44442222",
        "22444442",
        "55555555",  # 道
        "55555555",
        "55555555",
        "55555555",
        "55555555",
        "55555555",
        "55555555",
        "55555555"
    ])

# 迷路のデータ
maze = [
    "****************",
    "* **************",
    "* **************",
    "* **************",
    "* **************",
    "*    ***********",
    "* **  **********",
    "***  ***********",
    "*** ******** ***",
    "*** ***      ***",
    "*** *** ********",
    "***     ********",
    "******* ********",
    "******* ********",
    "******* ********",
    "****************"
]

# タイルマップへ迷路のデータを書き込む
# "*"" -> 0, " " -> 32 (16進法で020)
# イメージバンク (0,0)-(7, 7), (0,8)-(7,15) に対応
for y in range(len(maze)):
    row = maze[y]
    for x in range(len(row)):
        if row[x] == "*":
            pyxel.tilemap(0).set(x, y, ["000"])  # (0,0)-(7,7)
        elif row[x] == " ":
            pyxel.tilemap(0).set(x, y, ["020"])  # (0,8)-(7,15)


class Player:
    def __init__(self):
        self.x = 8
        self.y = 8

    def update(self):
        newx = self.x
        newy = self.y
        if pyxel.btnp(pyxel.KEY_RIGHT):
            newx += 8
        elif pyxel.btnp(pyxel.KEY_LEFT):
            newx -= 8
        elif pyxel.btnp(pyxel.KEY_UP):
            newy -= 8
        elif pyxel.btnp(pyxel.KEY_DOWN):
            newy += 8
        tile = pyxel.tilemap(0).get(newx//8, newy//8)
        if tile == 32:  # 道がある
            self.x = newx
            self.y = newy

    def draw(self):
        pyxel.rectb(self.x, self.y, 8, 8, 15)


def update():
    player.update()


def draw():
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 0, 0, 16, 16)
    player.draw()

player = Player()
pyxel.run(update, draw)
