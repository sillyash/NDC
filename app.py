import pyxel
from elements import Player

joueur = Player(20,20, 14, 11)
ennemis = []

WIDTH = 128
HEIGHT = 128

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Titre", fps=60, quit_key=pyxel.KEY_ESCAPE, display_scale=30)
        pyxel.load("theme.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        joueur.move()
        if pyxel.btnp(pyxel.KEY_SPACE):
            joueur.slash()
            joueur.draw_slash()

    def draw(self):
        pyxel.cls(0)
        joueur.draw()
        joueur.draw_life()
        pyxel.text(2,2, ("LVL - "+str(joueur.lvl)+"             SCORE - "+str(joueur.score)), 3)
        # pyxel.text(110,120, ("ENEMY LVL - "+str(max(ennemi.lvl) for ennemi in ennemis), 3))


App()
