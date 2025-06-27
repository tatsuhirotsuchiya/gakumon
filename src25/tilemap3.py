# タイルマップを使った例
import pyxel
import random
pyxel.init(256, 256)


# サウンド
pyxel.sounds[0].set("a3a2c1a1", "p", "7", "s", 5)

# グラフィックス
# イメージバンク0に，8x16のイメージを書き込む．座標(0, 24)を左上とする．
# (デフォルトで，イメージバンク0とタイルマップが対応
#  イメージバンク０以外をタイルマップにつかう場合は，tilemap.imgsrc(1)とか？)
# 注．リソースファイル使いたくないので．
# 普通はリソースファイルにグラフィックスを書いて，読み込むこと
pyxel.images[0].set(
    0,
    24,
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
# 文字1個をタイルマップ3x3，画面では24x24ピクセルに対応させる
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
# タイルマップは，全体で256x256 のサイズ
# タイルマップの各タイル(0,0)~(255,255)は，(10, 20)など値のタプル(ペア)を持つ
# タイルは 8x8 ピクセルのサイズ．(x, y) のタイルは，
# イメージマップの (x*8, y*8) から (x*8 + 7, y*8 + 7) の範囲を参照する．
# ここでは，壁のドット絵 (0, 24) から (7, 31)，道のドット絵 (0, 32) から (7, 39) なので，
# "*"" -> (0, 3), " " -> (0, 4) を，タイルマップの値にする
# (画像として表示するとき，
#  タイルマップの1点が，8x8ピクセルの画像になる．
#  (0, 3)は，イメージマップ0の(0, 24)-(7, 31)，
#  (0, 4)は，イメージマップ0の(0, 32)-(7, 39)
#  の部分が，切り取られて表示される)
for y in range(len(maze)):
    row = maze[y]
    for i in range(3):
        for x in range(len(row)):
            for j in range(3):
                if row[x] == "*":
                    pyxel.tilemaps[0].pset(3*x + j, 3*y + i, (0, 3))  # (0,3)=壁
                    if 3*x + j == 3 and 3*y + i == 3:
                        print(0, 3)
                elif row[x] == " ":
                    pyxel.tilemaps[0].pset(3*x + j, 3*y + i, (0, 4))  # (0,4)=道
                    if 3*x + j == 3 and 3*y + i == 3:
                        print(0, 4)


# タイルマップ上の座標をキャラの座標とする
# キャラの移動は3タイル単位＝24ピクセル単位としている
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
        # 3タイル単位で移動しているので，3倍する
        # 判定は，3x3タイルの左上のタイルしか見ていない
        (a, b) = pyxel.tilemaps[0].pget(3 * newx, 3 * newy)
        # 進める場合のみ移動
        if (a, b) == (0, 4):  # 道がある
            self.x = newx
            self.y = newy

    def draw(self):  # キャラの描画．24ピクセルごと移動
        pyxel.rectb(self.x * 24,  self.y * 24, 24, 24, 15)


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

        self.timer = random.randint(0, 5) + 4  # timerをリセット
        newx = self.x
        newy = self.y
        # 横向きの移動
        if target_x < self.x:
            newx -= 1
        if target_x > self.x:
            newx += 1
        # タイルマップから整数値のペア（タプル）を取得
        # 3タイル単位で移動しているので，3倍している
        # 判定は，3x3タイルの左上のタイルしか見ていない
        (a, b) = pyxel.tilemaps[0].pget(newx * 3, newy * 3)
        # 進める場合のみ移動
        if (a, b) != (0, 4):  # 道がない
            newx = self.x
        # 縦向きの移動 (横向きに移動しないとき)
        if self.x == newx and target_y < self.y:
            newy -= 1
        if self.x == newx and target_y > self.y:
            newy += 1
        # タイルマップから整数値のペア（タプル）を取得
        (a, b) = pyxel.tilemaps[0].pget(newx * 3, newy * 3)
        # 進める場合のみ移動
        if (a, b) != (0, 4):  # 道がない
            newy = self.y
        self.x = newx
        self.y = newy

    def draw(self):  # キャラの描画．24ピクセルごと移動
        pyxel.rectb(self.x * 24,  self.y * 24, 24, 24, 10)


class Treasure:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):  # キャラの描画
        pyxel.rectb(self.x * 24,  self.y * 24, 24, 24, 3)


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
    # カメラをキャラの位置に合わせる
    camera_x = max(0, min(player.x * 24 - 128, 384 - 256))
    camera_y = max(0, min(player.y * 24 - 128, 384 - 256))
    pyxel.camera(camera_x, camera_y)  # カメラをキャラの位置に合わせる
    print(camera_x, camera_y)

    # 画面をクリア
    pyxel.cls(0)
    # タイルマップを表示
    # bltm(x, y, tm, u, v, w, h, [colkey]
    pyxel.bltm(0, 0,  # 画面の(0, 0)を左上の座標として，
               0,  # タイルマップ0の
               0, 0,  # (0, 0)を左上の点として，
               384, 384)  # (384, 384)ピクセル分，つまり，16x16タイル分を描画
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
