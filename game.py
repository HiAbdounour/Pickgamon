from libx import * #pygame included
from random import randint as rdt, shuffle, choice as ch

# ajout couleur
cca=pygame.Color(155,225,247)

# classe principale
class Card:
    def __init__(self,value,pos,num,is_hidden=False):
        self.value = value
        self.x,self.y = pos
        if is_hidden:
            self.image = pygame.image.load("face card.png")
        else:
            self.image = pygame.image.load(value+" card.png")
        self.rect = self.image.get_rect()
        self.playernum = num
        self.rect.x += self.x
        self.rect.y += self.y
        if self.playernum == 2 or self.playernum == 3:
            self.rect.w = 120
            self.rect.h = 80

    def printscreen(self,screen):
        screen.blit(self.image,(self.x,self.y))
    def rotation(self,angle):
        self.image = pygame.transform.rotate(self.image,angle)

    def point_in_it(self,P):
        return self.rect.collidepoint(P.x,P.y)

# gestion des decks
values = ["greek","chinese","arabic","korean","topsxi","russian","charabia","egyptian","pick","don","spick","win","face"]
def distribue(win):
    """
    Distribue les cartes à chacun des joueurs
    Concrètement, renvoie un dictionnaire dont les clés sont les numéros des joueurs
    et la valeur associée une liste correspondant au deck du joueur.
    Remarque : le numéro 0 correspond à la pioche
    """
    ubro = ['greek']*4+['chinese']*4+['arabic']*4+['korean']*4+['topsxi']*4+['russian']*4+['charabia']*4+['egyptian']*4 # no special cards
    dico = {}
    for i in range(4):
        L = []
        for j in range(4):
            L.append(ubro.pop(rdt(0,len(ubro)-1)))
        dico[i+1] = L
    dico[0] = [elem for elem in ubro]
    dico[0] += ["pick","don","spick"]
    if win:
        dico[0]+=['win']
    shuffle(dico[0])
    return dico

def init_cst_pioche(b=0):
    """
    Renvoie une liste dont les POSITIONS correspondent aux numéros des joueurs
    et les éléments au nombre de pioches restantes pour chaque joueur
    b ne peut valoir que 0 ou 1, il correspond en binaire à la présence ou non
    de la carte spéciale Win
    """
    return [4+b]*4

# évènements
def detect_card(decks,P):
    """
    Renvoie la carte (type Card) qui a été cliquée par le joueur
    ainsi que le numéro du deck (type int), dans l'ordre (numéro,carte),
    None sinon
    P correspond au point cliqué
    decks correspond à l'ensemble des cartes virtuelles du jeu
    """
    for num in decks.keys():
        for card in decks[num]:
            if card.point_in_it(P):
                return num,card
    return None,None

def swing(numplayer,numadv,decks,cardR,cardD):
    """
    Simule le swing
    cardR : carte récupéré lors du swing, appartenant initialement à jADV
    cardD : carte donné en échange du swing, appartenant initialement à jPLAYER
    numplayer : numéro du joueur qui fait le swing
    numadv : numéro du joueur ciblé par le swing
    decks : decks du jeu
    """
    # Do not allow self swing - a priori already checked
    if numplayer != numadv and cardR != None and cardD != None:
        decks[numadv].remove(cardR)
        decks[numplayer].append(cardR)
        decks[numplayer].remove(cardD)
        decks[numadv].append(cardD)

def pioche(numplayer,decks,screen=None):
    """
    Simule la pioche d'une carte dans le deck pioche
    et lance le bonus si une carte spéciale est piochée
    numplayer est le numéro du joueur qui pioche
    decks sont les decks du jeu
    """
    value = decks[0].pop(0)
    decks[numplayer].append(value)
    if value == 'pick' or value == 'don':
        decks[numplayer].remove(value)
        text(f"Le joueur {numplayer} a pioché la carte spéciale {value}",yellow)
        attendre(1000)
        pickcard(numplayer,decks,value)
    if value == 'spick':
        decks[numplayer].remove('spick')
        text(f"Le joueur {numplayer} a pioché la carte spéciale spick",yellow)
        attendre(1000)
        sp = spickprocess(numplayer,screen,decks)
        return sp
    return (None,None)
        
def pickcard(numplayer,decks,pick_or_don):
    """
    Modélise l'action des cartes spéciales P!CK et Don
    numplayer est le numéro du joueur qui a pioché la carte spéciale
    pick_or_don vaut "pick" ou "don" et correspond à la carte en question
    decks sont les cartes du jeu
    """
    # Joueur 1
    if numplayer == 1:
        load_image("pickarea.png",Point(0,0))
        classed_decks = affiche_image(decks,screen)
        if pick_or_don == 'pick':
            t = "P!CKER"
        else:
            t = "DONNER"
        text(f"Choisissez une carte à {t}.")
        who = detect_card(classed_decks,wait_clic())
        while who[0] is None or who[0]==0 or (who[0]==1 and pick_or_don=="pick") or (who[0]!=1 and pick_or_don=="don"):
            error()
            who = detect_card(classed_decks,wait_clic())
        if pick_or_don == 'pick':
            decks[who[0]].remove(who[1].value)
            decks[1].append(who[1].value)
        else: # vaut don
            decks[1].remove(who[1].value)
            decks[rdt(2,4)].append(who[1].value)

    # Joueurs 2,3,4
    else:
        attacked = ch([i for i in range(1,5) if i!=numplayer])
        if pick_or_don == 'pick':
            card = ch(decks[attacked])
            decks[attacked].remove(card)
            decks[numplayer].append(card)
        else: # vaut don
            card = ch(decks[numplayer])
            decks[numplayer].remove(card)
            decks[attacked].append(card)

    # rafraîchissement
    load_image("pickarea.png",Point(0,0))
    affiche_image(decks,screen)
        
def spickprocess(num,screen,decks):
    """
    Permet la spick-isation d'une carte
    num est le numéro du joueur ayant pioché la carte SP!CK
    Concrètement, renvoie le tuple(num,value)
    où num est le numéro du joueur ayant la carte SP!CK
    et value la valeur de la carte spickée
    """
    if num==1:
        load_image("pickarea.png",Point(0,0))
        classed_decks = affiche_image(decks,screen)
        text("SP!CK une carte : elle ne pourra plus être volé !")
        who = detect_card(classed_decks,wait_clic())
        while who[0] is None or who[0]!=1:
            error()
            who = detect_card(classed_decks,wait_clic())
        return 1,who[1].value
    else:
        return num,ch(decks[num])

def is_spicked(sp,deckplayer,value,num,adv):
    """
    Renvoie True si la carte de valeur value est spickée
    sp est le tuple info du SP!CK
    num : joueur qui joue
    adv : joueur qui subit
    """
    if sp[1] != value:
        return False
    if sp[0] != num and sp[0] != adv:
        return False
    if deckplayer.count(sp[1]) == 1:
        if num==1:
            aff_pol("Carte spickée !",32,Point(280,400),red)
        return True
    return False


def detect_win(deckplayer):
    """
    Renvoie True si le joueur dont le deck est donné en argument
    contient les quatre cartes d'une même famille OU la carte WIN,
    False sinon
    """
    global values
    if deckplayer.count("win")==1:
        return True
    for elem in values[:8]:
        if deckplayer.count(elem)==4:
            return True
    return False

def choix_ia(nb_pioche):
    """
    Modélise l'action des joueurs 2,3 et 4 (IA)
    Concrètement, renvoie l'action réalisée par l'IA
    nb_pioche (type int) compte le nombre de coups de pioche disponibles pour le joueur
    """
    if nb_pioche != 0:
        return ch(['swing','swing','pioche','swing','swing'])
    else:
        return "swing"
    
def swing_ia(num,decks,sp):
    """
    Modélise le swing des joueurs 2,3 et 4 (IA)
    Concrètement, renvoie les cartes choisies pour le swing
    num est le numéro du joueur (2 ou 3 ou 4)
    decks : decks du jeu
    sp : infos sur la carte spickée
    """
    card_ia = ch(decks[num])
    while card_ia==sp[1] and sp[0]==num:
        card_ia = ch(decks[num])
    L = [1,2,3,4]
    L.remove(num)
    ennemi = ch(L)
    card_jE = ch(decks[ennemi])
    while card_jE==sp[1] and sp[0]==ennemi:
        card_jE = ch(decks[ennemi])
    return ennemi,card_jE,card_ia
    

# gestion graphique
def affiche_image(decks,screen,hidden=True):
    """
    Affiche les cartes (endroit ou envers) des decks des joueurs
    ainsi que la pioche
    hidden vaut True par défaut; doit valoir False UNIQUEMENT en cas de victoire
    Remarque : Définit les positions (point en haut à gauche) de chaque carte
    """
    virtual_decks = {0:[],1:[],2:[],3:[],4:[]}
    # Joueur 1
    i,j=320,585
    for card in decks[1]:
        c = Card(card,(i,j),1)
        c.printscreen(screen)
        virtual_decks[1].append(c)
        i+=82
    # Joueur 2
    i,j = 15,20
    for card in decks[2]:
        c = Card(card,(i,j),2,hidden)
        c.rotation(-90)
        c.printscreen(screen)
        virtual_decks[2].append(c)
        j+=82
    # Joueur 3
    i,j = 1110,590
    for card in decks[3]:
        c = Card(card,(i,j),3,hidden)
        c.rotation(90)
        c.printscreen(screen)
        virtual_decks[3].append(c)
        j-=82
    # Joueur 4
    i,j = 820,-20
    for card in decks[4]:
        c = Card(card,(i,j),4,hidden)
        c.rotation(180)
        c.printscreen(screen)
        virtual_decks[4].append(c)
        i -= 82
    # Pioche
    if decks[0] != []:
        i,j = 600,240
        c = Card(decks[0][0],(i,j),0,True)
        c.printscreen(screen)
        virtual_decks[0].append(c)
    return virtual_decks

def text(txt,clr=cca):
    """
    Affiche un texte pour le joueur 1
    clr est la couleur du texte (teinte bleu clair par défaut)
    """
    aff_pol(txt,32,Point(280,500),clr)
    
def print_txt_actionj1(pioche_possible=True):
    """
    """
    if pioche_possible:
        text("Choisissez une carte d'un de vos adversaires ou piochez.")
    else:
        text("Quotat de pioche épuisé ! Choisissez une carte d'un de vos adversaires.")

def print_winactive(b):
    """
    """
    if b:
        t = "ON"
    else:
        t = "OFF"
    aff_pol(t,50,Point(800,20),orange)

# Bande sonore
def error():
    play_sound("buzz.mp3")

def lobby():
    load_music("pickosong.mp3")
    play_music(1)

# Core game
def init_game(win):
    """
    Initialise les variables nécessaires au jeu
    """
    decks = distribue(win)
    b=0
    if win:
        b=1
    can_pioche = init_cst_pioche(b)
    n_is_playing = 1
    end_game,winner = False,None
    sp = (None,None)
    return decks,can_pioche,n_is_playing,end_game,winner,sp


# Debug
def print_point(P):
    print(P.x,P.y)


#=======================BEGIN===========================
screen = init_graphic(1250,710,"Pickgamon")#,fullscreen=True)
load_image("pickarea.png",Point(0,0))
menu = 0 # 0 = menu, 1 = jeu, -1 = settings
idplay = 0
winactive = False
lobby()

running = True
while running:
    # HOME :
    if menu==0:
        load_image("pickarea.png",Point(0,0))
        load_image_transp("PICKOGO.png",Point(100,0))
        aff_pol("Appuyer sur ESPACE pour commencer à jouer",32,Point(200,600),cca)
        aff_pol("Appuyer sur P pour modifier les paramètres",32,Point(200,650),cca)

    # GAME :
    elif menu==1:
        load_image("pickarea.png",Point(0,0))
        if idplay == 0: #initialisation
            decks,can_pioche,n_is_playing,end_game,winner,sp = init_game(winactive)
            idplay = 1
        if not end_game:
            # Affichage
            classed_decks = affiche_image(decks,screen)
            attendre(1000)

            # ===== [The Game] =====
            # Joueur 1
            if n_is_playing == 1:
                # Choix
                print_txt_actionj1(can_pioche[0] != 0)
                num,choosed_card = detect_card(classed_decks,wait_clic())
                us = False
                if sp!=(None,None):
                    us=is_spicked(sp,decks[sp[0]],choosed_card.value,1,num)
                    while us:
                        num,choosed_card = detect_card(classed_decks,wait_clic())
                        us=is_spicked(sp,decks[sp[0]],choosed_card.value,1,num)
                while num is None or num == 1 or (num==can_pioche[0]==0):
                    error()
                    num,choosed_card = detect_card(classed_decks,wait_clic())

                # Actualisation
                load_image("pickarea.png",Point(0,0))
                classed_decks = affiche_image(decks,screen)

                # Pioche
                if num == 0:
                    sp = pioche(1,decks,screen)
                    can_pioche[0] -= 1
                    if detect_win(decks[1]):
                        end_game,winner = True,1
                # Swing
                else: #num vaut 2,3 ou 4
                    text("Choisissez la carte de votre deck que vous souhaitez échanger.")
                    binnum,given_card = detect_card(classed_decks,wait_clic())
                    while binnum !=1 or binnum is None:
                        error()
                        binnum,given_card = detect_card(classed_decks,wait_clic())
                    swing(1,num,decks,choosed_card.value,given_card.value)
                    if num != 0 and detect_win(decks[num]):
                        end_game,winner = True,num
                    if detect_win(decks[1]):
                        end_game,winner = True,1
                # Passage anticipé au joueur suivant
                if winner is None:
                    n_is_playing = 2
                    load_image("pickarea.png",Point(0,0))
                    classed_decks = affiche_image(decks,screen)
                    attendre(1000)

            # Joueurs 2,3 et 4
            elif n_is_playing == 2 or n_is_playing == 3 or n_is_playing == 4:
                action = choix_ia(can_pioche[n_is_playing-1])
                if action == "pioche":
                    sp = pioche(n_is_playing,decks,screen)
                    can_pioche[n_is_playing-1]-=1
                    if detect_win(decks[n_is_playing]):
                        end_game,winner = True,n_is_playing
                else: # action vaut "swing"
                    adv,choosed_value,given_value = swing_ia(n_is_playing,decks,sp)
                    swing(n_is_playing,adv,decks,choosed_value,given_value)
                    if detect_win(decks[adv]):
                        end_game,winner = True,adv
                    if detect_win(decks[n_is_playing]):
                        end_game,winner = True,n_is_playing
                # Joueur suivant
                n_is_playing += 1

            else: #théoriquement atteint lorsque n_is_playing vaut 5
                n_is_playing = 1
            # Actualisation des évènements
            load_image("pickarea.png",Point(0,0))

        # victoire
        if end_game:
            text(f"Le joueur {winner} a gagné !")
            deckend = {i:[] for i in range(5)}
            deckend[winner] = decks[winner]
            classed_decks = affiche_image(deckend,screen,False)
            attendre(3000)
            menu = 0
            lobby()

    # SETTINGS :
    elif menu==-1:
        load_image("pickarea.png",Point(0,0))
        aff_pol("Dés/Activer la carte WIN (touche W)",50,Point(150,20),cca)
        aff_pol("Quitter le jeu (touche Échap)",50,Point(150,100),cca)
        aff_pol("Revenir au menu (touche Z)",50,Point(150,220),cca,True)
        print_winactive(winactive)


    # NONE :
    else:
        pass


    for event in pygame.event.get():
        # Fermeture de la fenêtre - Fin définitive
        if event.type == pygame.QUIT:
            running = False
            stop_music()
            pygame.quit()
        elif event.type == KEYDOWN:
            # Fermeture de la fenêtre - Fin définitive
            if event.key == K_ESCAPE:
                running = False
                stop_music()
                pygame.quit()
            # Lancer le jeu
            elif event.key == K_SPACE and menu==0:
                menu = 1
                idplay = 0
                lobby()
            # Paramètres
            elif event.key == K_p and menu!=1:
                menu = -1
            # Revenir au menu
            elif event.key == K_z and menu==-1:
                menu = 0
            # Dés/Activer la carte WIN
            elif event.key == K_w and menu==-1:
                winactive = not winactive
            

    pygame.display.flip()




