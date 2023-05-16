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
    def __init__(self):
        self.tir = False
        self.life = 3
        self.score = 0

    def draw_visor(self):
        pyxel.circb(x, y, 4, )
        if self.tir:
            pyxel.circb(x, y, 4,)

    def draw_life(self):
        for i in range(self.life):
            pyxel.rect(2 + i * 15, 10, 10, 10, 9)

    def fire(self, target):
        self.tir = pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
        if self.tir and self.hit(target):
            return True

    def hit(self, target):
        return pyxel.mouse_x > target.x and pyxel.mouse_y > target.y and \
            pyxel.mouse_x < target.x + target.w and \
            pyxel.mouse_y < target.y + target.h
