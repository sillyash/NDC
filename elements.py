import pyxel

# on crée une liste, chaque index correspondant à un "niveau" et taille du slime (de 0 à 4),
# contenant les coordonnées de son sprite sur la bangue d'images.
sprites = [(1,4,14,12), (0,19,16,14), (0,41,18,17), (), ()]

# on crée un dictionnaire, chaque clé correspond à la direction du coup, et chaque
# index la frame (de 0 à 2) pour cette direction, contenant les coordonées sur lka banque d'images.
slash = {
    "up": [[241,61,5,3], [241,76,9,4], [241,92,14,4]],
    "down": [[245,63,-5,-3], [249,79,-9,-4], [254,95,-14,-4]],
    "left": [[231,9,3,5], [228,25,4,9], [228,41,4,14]],
    "right": [[248,9,3,5], [248,25,4,9], [248,41,4,14]]
}


class Player:
    def __init__(self, x, y):
        self.lvl = 0
        self.x = x
        self.y = y
        self.w = sprites[self.lvl][2]
        self.h = sprites[self.lvl][3]
        self.life = 3
        self.score = 0
        self.dir = "up"

    def move(self):
        if pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.KEY_UP):
            self.y -= 0.5
            self.dir = "up"
        if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
            self.y += 0.5
            self.dir = "down"
        if pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 0.5
            self.dir = "left"
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 0.5
            self.dir = "right"

    def draw(self):
        pyxel.blt(self.x, self.y, 0, sprites[self.lvl][0], sprites[self.lvl][1], sprites[self.lvl][2], sprites[self.lvl][3], 0)

    def draw_life(self):
        for i in range(self.life):
            pyxel.rect(3 + i * 6, 120, 5, 5, 4)

    def is_hit(self, target)->bool:
        if self.dir == "up":
            return target.y+target.h >= self.y >= target.y+target.h+4 and target.x+target.w >= self.x >= target.x
        if self.dir == "down":
            return target.y >= self.y >= target.y-4 and target.x+target.w >= self.x >= target.x
        if self.dir == "left":
            return target.x+target.w+4 >= self.x >= target.x+target.w and target.y+target.h >= self.y >= target.y
        if self.dir == "right":
            return target.x >= self.x >= target.x-4 and target.y+target.h >= self.y >= target.y

    def slash(self, target):
        target.life -= 1
        self.score += 3
        target.draw_hit()
        if self.score%21 == 0 and self.lvl < 5:
            self.lvl += 1

    def draw_slash(self):
        pyxel.blt(self.x, self.y, 0, slash[self.dir][0][0], slash[self.dir][0][1], slash[self.dir][0][2], slash[self.dir][0][3])
        pyxel.blt(self.x, self.y, 0, slash[self.dir][1][0], slash[self.dir][1][1], slash[self.dir][1][2], slash[self.dir][1][3])
        pyxel.blt(self.x, self.y, 0, slash[self.dir][2][0], slash[self.dir][2][1], slash[self.dir][2][2], slash[self.dir][2][3])
        pyxel.blt(self.x, self.y, 0, slash[self.dir][3][0], slash[self.dir][3][1], slash[self.dir][3][2], slash[self.dir][3][3])

    def draw_hit(self):
        pyxel.blt(self.x, self.y, 1, sprites[self.lvl][0], sprites[self.lvl][1], sprites[self.lvl][2], sprites[self.lvl][3], 0)


class Enemy:
    def __init__(self, x, y):
        self.lvl = 0
        self.x = x
        self.y = y
        self.w = sprites[self.lvl][2]
        self.h = sprites[self.lvl][3]
        self.life = 3
        self.score = 0

    def move(self, target):
        while not self.is_hit(target):
            if self.y+self.w < target.y:
                self.y += 0.5
            if self.y > target.y+target.w:
                self.y -= 0.5
            if self.x+self.w < target.x:
                self.x += 0.5
            if self.x > target.x+target.w:
                self.x -= 0.5

    def draw(self):
        pyxel.blt(self.x, self.y, 0, sprites[self.lvl][0]+40, sprites[self.lvl][1], sprites[self.lvl][2], sprites[self.lvl][3], 0)

    def draw_life(self):
        for i in range(self.life):
            pyxel.rect(3 + i * 6, 120, 5, 5, 4)

    def is_hit(self, target)->bool:
        return target.x+target.w >= self.x >= target.x and target.y+target.h >= self.y >= target.y

    def draw_attack(self):
        for i in range(6):
            self.y += 0.5
        for i in range(2):
            self.y -= 1.5

    def attack(self, target):
        target.life -= 1
        target.draw_hit()

    def draw_hit(self):
        pyxel.blt(self.x, self.y, 1, sprites[self.lvl][0]+40, sprites[self.lvl][1], sprites[self.lvl][2], sprites[self.lvl][3], 0)
