import pyxel
from elements import Player

joueur = Player(74,26)
ennemis = []

WIDTH = 128
HEIGHT = 72

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Titre", fps=60, quit_key=pyxel.KEY_ESCAPE, display_scale=14)
        pyxel.load("theme.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        joueur.draw()
        

App()
