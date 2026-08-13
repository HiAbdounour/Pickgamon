"""
Extraits du module graphique pour NSI
Les fonctions ci-dessous appartiennent à leurs auteurs respectifs
Auteurs : M. Boehm & P. Remy (améliorations : L. Rebmeister),
          Lycée Les Pierres Vives, Carrières-sur-Seine
Version 4.1 du 14/10/18
"""

import pygame
from pygame.locals import *

pygame.init()

PYGAME_SDL_AFFICHAGE=1
PYGAME_SDL_FONT="segoeuiscript"

black=pygame.Color(0,0,0)
blue=pygame.Color(0,0,255)
brown=pygame.Color(88,41,0)
cyan=pygame.Color(0,255,255)
gold=pygame.Color(255,215,0)
gray=pygame.Color(128,128,128)
green=pygame.Color(0,255,0)
magenta=pygame.Color(255,0,255)
orange=pygame.Color(255,127,0)
pink=pygame.Color(253,108,158)
purple=pygame.Color(127,0,255)
red=pygame.Color(255,0,0)
salmon=pygame.Color(248,142,85)
silver=pygame.Color(206,206,206)
turquoise=pygame.Color(37,253,233)
white=pygame.Color(255,255,255)
yellow=pygame.Color(255,255,0)
def couleur_RGB(r,g,b) :
    """
    Renvoie une couleur RGB.
    r (compris entre 0 et 255) est la quantité de rouge
    g (compris entre 0 et 255) est la quantité de vert
    b (compris entre 0 et 255) est la quantité de bleu
    """
    return pygame.Color(r,g,b)

def init_graphic(W,H,name="Fenêtre ISN",bg_color=black,fullscreen=0) :
    """
    Initialise la fenêtre graphique.
    W est la largeur et H est la hauteur
    name est le nom de la fenêtre (par défaut Fenêtre ISN).
    bg_color est la couleur de l'arrière-plan (par défaut noir).
    fullscreen affiche la fenêtre de taille W*H si la valeur est 0 (par défaut)
    et en plein écran pour une autre valeur.
    L'origine (0,0) de la fenêtre graphique est situé en haut à gauche.
    """
    global PYGAME_SDL_WINDOW,PYGAME_SDL_WEIGHT,PYGAME_SDL_HEIGHT,PYGAME_SDL_BGCOLOR
    PYGAME_SDL_WEIGHT = W; PYGAME_SDL_HEIGHT = H
    PYGAME_SDL_BGCOLOR = bg_color
    if fullscreen == 0:
        PYGAME_SDL_WINDOW = pygame.display.set_mode((int(W),int(H)))
    else:
        PYGAME_SDL_WINDOW = pygame.display.set_mode((int(W),int(H)),FULLSCREEN)
    pygame.display.set_caption(name)
    pygame.draw.rect(PYGAME_SDL_WINDOW,bg_color,(0,0,int(W),int(H)),0)
    pygame.display.flip()
    return PYGAME_SDL_WINDOW

def load_image(F,P) :
    """
    Affiche une image.
    F est une chaîne de caractère donnant le nom du fichier image.
    P est le point en haut à gauche de l'image.
    Renvoie l'image sous forme de surface pygame.
    """
    P.x = int(P.x); P.y = int(P.y)
    fond = pygame.image.load(F).convert()
    PYGAME_SDL_WINDOW.blit(fond,(P.x,P.y))
    return fond

def affiche_all() :
    """
    Affiche les tracés de formes
    """
    pygame.display.flip()

def attendre(millisecondes) :
    """
    Attend le nombre de millisecondes passé en argument
    """
    # Modification Loïc
    if PYGAME_SDL_AFFICHAGE == 1 :
        affiche_all()

    pygame.time.delay(millisecondes)

class Point :
    """
    Cette classe définit un point prenant deux champs x et y.
    P.x est l'abscisse du point P.
    P.y est l'ordonnée du point P.
    On écrira P=Point(10,50) pour définir le point P de coordonnées (10,50).
    """
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    # Ajout Loïc
    def __eq__(self, other) :
        """
        Rend le P1 == P2 fonctionnel
        """
        if isinstance(other, Point) :
            return self.x == other.x and self.y == other.y
        return False

    # Ajout Loïc
    def __ne__(self, other) :
        """
        Rend le P1 != P2 fonctionnel
        """
        return not self.__eq__(other)

    # Ajout Loïc
    def __str__(self) :
        """
        Permet d'écrire des points dans la console
        """
        return "("+str(self.x)+", "+str(self.y)+")"

def wait_clic() :
    """
    Attend que l'on clique gauche avec la souris.
    Renvoie les coordonnées du point cliqué.
    Instruction bloquante.
    """
    # Ajout Loïc
    if PYGAME_SDL_AFFICHAGE == 1 :
        affiche_all()

    pygame.event.clear()

    while 1 :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                return pygame.quit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                return Point(event.pos[0],event.pos[1])

def aff_pol(T,t,P,C,text_bold=False,text_italic=False) :
    """
    Affiche une chaîne de caractère T en police Verdana à la taille t.
    P est le point en haut à gauche
    C est la couleur d'affichage.
    Les arguments text_bold (gras) et text_italic (italique) sont optionnels.
    """
    P.x = int(P.x); P.y = int(P.y)
    font = pygame.font.SysFont(PYGAME_SDL_FONT,t,bold=text_bold,italic=text_italic)
    text = font.render(T,1,C)
    PYGAME_SDL_WINDOW.blit(text,(P.x,P.y))

def play_sound(F) :
    """
    F est une chaîne de caractères contenant le nom du fichier son.
    Joue le son F.
    """
    pygame.mixer.Sound(F).play()

def load_music(F) :
    """
    F est une chaîne de caractères contenant le nom du fichier audio.
    Charge la musique F mais ne la joue pas.
    Si une musique était déjà chargée, cela la stoppe si elle etait jouée.
    Utiliser de préférence des .wav
    """
    pygame.mixer.music.load(F)

def play_music(loop=0) :
    """
    Lance la musique. Si la musique était déjà jouée, elle reprend au début
    L'argument optionnel loop prend les valeurs 0 ou 1.
    Si loop vaut 1, alors la musique est jouée en boucle.
    """
    if loop == 1:
        pygame.mixer.music.play(loops=-1)
    else:
        pygame.mixer.music.play()

def load_image(F,P) :
    """
    Affiche une image.
    F est une chaîne de caractère donnant le nom du fichier image.
    P est le point en haut à gauche de l'image.
    Renvoie l'image sous forme de surface pygame.
    """
    P.x = int(P.x); P.y = int(P.y)
    fond = pygame.image.load(F).convert()
    PYGAME_SDL_WINDOW.blit(fond,(P.x,P.y))
    return fond

def load_image_transp(F,P) :
    """
    Affiche une image à transparence.
    F est une chaîne de caractère donnant le nom du fichier image.
    P est le point en haut à gauche de l'image.
    Renvoie l'image sous forme de surface pygame.
    """
    P.x = int(P.x); P.y = int(P.y)
    fond = pygame.image.load(F).convert_alpha()
    PYGAME_SDL_WINDOW.blit(fond,(P.x,P.y))
    return fond

def stop_music() :
    """
    Arrête la musique.
    """
    pygame.mixer.music.stop()
