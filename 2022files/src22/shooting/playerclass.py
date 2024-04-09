import pyxel


class Player:
    def __init__(self):
        self.x = 120
        self.y = 120

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = max(self.x - 4, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = min(self.x + 4, 240)
        if pyxel.btn(pyxel.KEY_UP):
            self.y = max(self.y - 4, 0)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y = min(self.y + 4, 240)

    def draw(self):
        # イメージバンク0の座標(0,0)から16x16ドットを取ってきて
        # プレーヤー（飛行機）として表示
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)
