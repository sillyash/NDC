import pyxel
from elements import Player, Enemy

joueur = Player(70, 70)
ennemis = [Enemy(0,0)]
sprites = [(1,4,14,12), (0,19,16,14), (0,41,18,17), (0,61,79,19), (0,83,25,21)]

WIDTH = 128
HEIGHT = 128

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Titre", fps=60, quit_key=pyxel.KEY_ESCAPE, display_scale=30)
        pyxel.load("theme.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        # spawn d'ennemis
        if pyxel.frame_count%120 == 0:
            for ennemi in ennemis:
                ennemi.score += 3
            x = pyxel.rndi(1,2)
            if x == 1:
                ennemis.append(Enemy(pyxel.rndi(5,120), 5))
            if x == 2:
                ennemis.append(Enemy(5, pyxel.rndi(5,120)))
                ennemis.append(Enemy(5, pyxel.rndi(5,120)))

        # déplacements
        joueur.move()
        for ennemi in ennemis:
            ennemi.move(joueur)

        # attaque joueur
        if pyxel.btnp(pyxel.KEY_SPACE):
            joueur.draw_slash()
            for ennemi in ennemis:
                if joueur.is_hit(ennemi):
                    joueur.slash(ennemi)
                    ennemis.remove(ennemi)

        # attaque ennemie (auto & toutes les 2sec)
        if pyxel.frame_count%120 == 0:
            for ennemi in ennemis:
                ennemi.draw_attack()
                if ennemi.is_hit(joueur):
                    ennemi.attack(joueur)

        # niveaux
        joueur.w = sprites[joueur.lvl][2]
        joueur.h = sprites[joueur.lvl][3]
        for ennemi in ennemis:
            ennemi.w = sprites[ennemi.lvl][2]
            ennemi.h = sprites[ennemi.lvl][3]

    def draw(self):
        pyxel.cls(0)
        for ennemi in ennemis:
            ennemi.draw()
        joueur.draw()
        joueur.draw_life()
        pyxel.text(2,2, ("LVL - "+str(joueur.lvl)+"             SCORE - "+str(joueur.score)), 3)


App()
