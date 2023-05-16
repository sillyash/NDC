import pyxel
from elements import Player, Enemy

joueur = Player(70, 70)
ennemis = [Enemy(0,0), Enemy(0,50)]
sprites = [(1,4,14,12), (0,19,16,14), (0,41,18,17), (), ()]

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
            x = pyxel.rndi(1,6)
            if x == 1:
                ennemis.append(Enemy(pyxel.rndi(5,120), 5))
            if x == 2:
                ennemis.append(Enemy(5, pyxel.rndi(5,120)))
                ennemis.append(Enemy(5, pyxel.rndi(5,120)))
            if x == 3:
                ennemis.append(Enemy(5, pyxel.rndi(5,120)))
                ennemis.append(Enemy(5, pyxel.rndi(5,120)))
            if x == 4:
                ennemis.append(Enemy(pyxel.rndi(5,120, 5)))

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
        joueur.draw()
        joueur.draw_life()
        pyxel.text(2,2, ("LVL - "+str(joueur.lvl)+"             SCORE - "+str(joueur.score)), 3)
        # pyxel.text(110,120, ("ENEMY LVL - "+str(max(ennemi.lvl) for ennemi in ennemis), 3))


App()
