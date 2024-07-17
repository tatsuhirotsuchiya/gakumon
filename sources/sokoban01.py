import pyxel
import random
pyxel.init(128, 128)

# サウンド
pyxel.sounds[0].set("a3a2c1a1", "p", "7", "s", 5)

# グラフィックス
# イメージバンク0に8x16のイメージを書き込む．座標0,0を左上とする．
# (デフォルトで，イメージバンク0とタイルマップが対応
#  イメージバンク０以外をタイルマップにつかう方法はよくわからない)
pyxel.images[0].set(
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
    "*              *",
    "* ***** **** * *",
    "* **         * *",
    "* ** ******* * *",
    "*    ******  * *",
    "* **     *** * *",
    "* *  *** ***   *",
    "* * **** *** * *",
    "* * ***      * *",
    "* * *** ****** *",
    "* *     **     *",
    "* * ***    * * *",
    "* * *** **** * *",
    "*              *",
    "****************"
]

# タイルマップ０へ迷路のデータを書き込む
# タイルマップは，256x256 のサイズ．
# タイルマップの各点(0,0)~(255,255)は，(10, 20)など値のタプル（対）
# ここでは，"*"" -> (0, 0), " " -> (0, 1) として書込み
# (画像として表示するとき，
#  タイルマップの1点が，8x8ピクセルの画像になる．
#  (0,0)は，イメージマップ0の(0,0)-(7,7)，
#  (0,1)は，イメージマップ0の(0,8)-(7,15)
#  の部分が，切り取られて表示される)
for y in range(len(maze)):
    row = maze[y]
    for x in range(len(row)):
        if row[x] == "*":
            pyxel.tilemaps[0].set(x, y, ["0000"])  # (0,0)
        elif row[x] == " ":
            pyxel.tilemaps[0].set(x, y, ["0001"])  # (0,1)


# タイルマップ上の座標をキャラの座標とする
# つまり，キャラの移動は1タイル単位＝8ピクセル単位
class Player:
    def __init__(self):  # キャラの初期座標を設定
        self.x = 1
        self.y = 1

    def update(self):  # キャラの移動
        dx = 0
        dy = 0
        if pyxel.btnp(pyxel.KEY_RIGHT):
            dx = 1
        elif pyxel.btnp(pyxel.KEY_LEFT):
            dx = -1
        elif pyxel.btnp(pyxel.KEY_UP):
            dy = -1
        elif pyxel.btnp(pyxel.KEY_DOWN):
            dy = 1
        else:
            return
        
        # タイルマップから整数値のペア（タプル）を取得
        (a, b) = pyxel.tilemaps[0].pget(x + dx, y + dy)
        (c, d) = pyxel.tilemaps[0].pget(x + dx + dx, y + dy + dy)

        # 動かすボックスを確認
        box_to_move = None
        for box in boxes:
            if box.x == x + dx and box.y == y + dy:
                box_to_move = box
                break
        box_to_block = None
        if box_to_move != None:
            for box in boxes:
                if box.x == x + dx + dx and box.y == y + dy + dy:
                    box_to_block = box
                    break
        
        # 進める，かつ，箱がない
        if (a, b) == (0, 1) and box_to_move == None:
            self.x += dx
            self.y += dy
        elif (a, b) == (0, 1) and box_to_move and box_to_block == None:  # 進める，かつ，箱がある
            s



    def draw(self):  # キャラの描画．8ピクセルごと移動
        pyxel.rectb(self.x * 8,  self.y * 8, 8, 8, 15)


class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 座標設定
    def set(self, x, y):
        self.x = x
        self.y = y

        '''
        # タイルマップから整数値のペア（タプル）を取得
        (a, b) = pyxel.tilemaps[0].pget(newx, newy)
        # 進める場合のみ移動
        if (a, b) != (0, 1):  # 道がない
            newy = self.y
        self.x = newx
        self.y = newy
        '''

    def draw(self):  # キャラの描画．8ピクセルごと移動
        pyxel.rectb(self.x * 8,  self.y * 8, 8, 8, 10)


def update():
    global treasure, score
    player.update()
    for m in monsters:
        m.update(player.x, player.y)
    isDead = False
    for m in monsters:
        if m.x == player.x and m.y == player.y:
            isDead = True
    if isDead:
        pyxel.play(0, 0)
        gamestart()
    if treasure.x == player.x and treasure.y == player.y:
        pyxel.play(0, 0)
        y = random.randint(1, 14)
        treasure = Treasure(14, y)
        score += 1


def draw():
    pyxel.cls(0)
    # タイルマップを表示
    # bltm(x, y, tm, u, v, w, h, [colkey]
    pyxel.bltm(0, 0,  # 画面の(0, 0)を左上の座標として，
               0,  # タイルマップ0の
               0, 0,  # (0, 0)を左上の点として，
               128, 128)  # (128, 128)ピクセル分，つまり，16x16タイル分を描画
    player.draw()
    for m in monsters:
        m.draw()
    treasure.draw()
    pyxel.text(5, 4, str(score), 15)


player = Player()
monsters = []
treasure = Treasure(14, 2)
score = 0


def gamestart():
    global player, monsters, treasure, score
    player = Player()
    monsters = []
    for i in range(4):
        monsters.append(Monster(14, i + 1))
    treasure = Treasure(14, 2)
    score = 0


gamestart()
pyxel.run(update, draw)
