import pyxel
from elements import Player

joueur = Player()
ennemis = []

WIDTH = 128
HEIGHT = 72

# on crée une liste, chaque index correspondant à un "niveau" et taille du personnage,
# contenant les coordonnées de son sprite sur la bangue d'images.
sprites = [(1,4,14,11),(0,19,16,13),(0,41,18,16)]
slash = {
    "up": [(241,61,5,3), (241,76,9,4), (241,92,14,4)]
    "down": [(245,63,-5,-3), (249,79,-9,-4), (254,95,-14,-4)]
    "left": [(231,9,3,5), (228,25,4,9), (228,41,4,14)]
    "right": [(248,9,3,5), (248,25,4,9), (248,41,4,14)]
}

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Titre", fps=60, quit_key=pyxel.KEY_ESCAPE, """display_scale=14""")
        pyxel.load("theme.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        joueur.draw()
        pass

App()
