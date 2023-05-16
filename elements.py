import pyxel

# on crée une liste, chaque index correspondant à un "niveau" et taille du slime (de 0 à 4),
# contenant les coordonnées de son sprite sur la bangue d'images.
sprites = [(1,4,14,11), (0,19,16,13), (0,41,18,16), (), ()]

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
        self.x = x
        self.y = y
        self.life = 3
        self.score = 0
        self.lvl = 0
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
        pyxel.blt(self.x, self.y, 0, sprites[self.lvl][0], sprites[self.lvl][1], \
            sprites[self.lvl][2], sprites[self.lvl][3], 0)

    def draw_life(self):
        for i in range(self.life):
            pyxel.rect(3 + i * 6, 120, 5, 5, 4)

    def draw_slash(self):
        pass


class Enemy:
    def __init__(self, x, y, score):
        self.lvl = score//24
        self.life = 3 + lvl
        self.coord = (x, y)