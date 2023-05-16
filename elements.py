import pyxel


class Car:
    def __init__(self, x, y, w, h, life, sprite):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.life = life
        self.sprite = sprite
        self.sheet = True

    def move(self):
        self.x += 1

    def draw(self):
        if self.life > 0:
            pass
        pass


class Player:
    def __init__(self, x, y):
        self.tir = False
        self.life = 3
        self.score = 0
        self.coord = (x,y)

    def draw(self, lvl):
        #pyxel.blt()

    def move(self):
        if pyxel.btnp(KEY_Z) or pyxel.btnp(KEY_UP):
            self.coord = (x, y-2)
        if pyxel.btnp(KEY_S) or pyxel.btnp(KEY_DOWN):
            self.coord = (x, y+2)
        if pyxel.btnp(KEY_Q) or pyxel.btnp(KEY_LEFT):
            self.coord = (x-2, y)
        if pyxel.btnp(KEY_D) or pyxel.btnp(KEY_RIGHT):
            self.coord = (x+2, y)

    def draw_life(self):
        for i in range(self.life):
            pyxel.rect(2 + i * 15, 10, 10, 10, 9)
