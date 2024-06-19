import pyxel
pyxel.init(128, 128)

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
    "* **************",
    "* ********** ***",
    "* ********** ***",
    "* ********** ***",
    "*    ******  ***",
    "* **  ****** ***",
    "***  ******* ***",
    "*** ******** ***",
    "*** ***      ***",
    "*** *** ********",
    "***     ********",
    "******* ********",
    "******* ********",
    "******* ********",
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
        newx = self.x
        newy = self.y
        if pyxel.btnp(pyxel.KEY_RIGHT):
            newx += 1
        elif pyxel.btnp(pyxel.KEY_LEFT):
            newx -= 1
        elif pyxel.btnp(pyxel.KEY_UP):
            newy -= 1
        elif pyxel.btnp(pyxel.KEY_DOWN):
            newy += 1
        # タイルマップから整数値のペア（タプル）を取得
        (a, b) = pyxel.tilemaps[0].pget(newx, newy)
        # 進める場合のみ移動
        if (a, b) == (0, 1):  # 道がある
            self.x = newx
            self.y = newy

    def draw(self):  # キャラの描画．8ピクセルごと移動
        pyxel.rectb(self.x * 8,  self.y * 8, 8, 8, 15)


class Monster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = 10

    # 主人公の座標を追う
    def update(self, target_x, target_y):
        # timerが0のときだけ動作
        if self.timer > 0:
            self.timer -= 1
            return

        self.timer = 10  # timerをリセット
        newx = self.x
        newy = self.y
        # 横向きの移動
        if target_x < self.x:
            newx -= 1
        if target_x > self.x:
            newx += 1
        # タイルマップから整数値のペア（タプル）を取得
        (a, b) = pyxel.tilemaps[0].pget(newx, newy)
        # 進める場合のみ移動
        if (a, b) != (0, 1):  # 道がない
            newx = self.x
        # 縦向きの移動 (横向きに移動しないとき)
        if self.x == newx and target_y < self.y:
            newy -= 1
        if self.x == newx and target_y > self.y:
            newy += 1
        # タイルマップから整数値のペア（タプル）を取得
        (a, b) = pyxel.tilemaps[0].pget(newx, newy)
        # 進める場合のみ移動
        if (a, b) != (0, 1):  # 道がない
            newy = self.y
        self.x = newx
        self.y = newy

    def draw(self):  # キャラの描画．8ピクセルごと移動
        pyxel.rectb(self.x * 8,  self.y * 8, 8, 8, 10)


def update():
    player.update()
    monster1.update(player.x, player.y)


def draw():
    pyxel.cls(0)
    # タイルマップを表示
    # bltm(x, y, tm, u, v, w, h, [colkey]
    pyxel.bltm(0, 0,  # 画面の(0, 0)を左上の座標として，
               0,  # タイルマップ0の
               0, 0,  # (0, 0)を左上の点として，
               128, 128)  # (128, 128)ピクセル分，つまり，16x16タイル分を描画
    player.draw()
    monster1.draw()


player = Player()
monster1 = Monster(12, 3)
pyxel.run(update, draw)
