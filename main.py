import pygame
import sys
import traceback# Module de vérification des erreurs
from pygame.locals import *#import pygame tous les modules
import MyPlane
import enemy
import bullet
from random import *
import supply


pygame.init()
pygame.mixer.init()

bg_size = width, height = 901,897
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("Jeu de bataille")
#Image de fond
background = pygame.image.load("image/bg.png").convert()

#Couleurs
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

#Module de temps
clock = pygame.time.Clock()

#charger la musique du jeu
pygame.mixer.music.load("sound/bg_music.wave")#Musique de fond
pygame.mixer.music.set_volume(0.1)
hit = pygame.mixer.Sound("sound/hit.wav") # l'effet sonore "frapper"
hit.set_volume(0.2)
winner = pygame.mixer.Sound("sound/winner.wav") #musique de victoire de jeu
winner.set_volume(0.2)
big_enemy = pygame.mixer.Sound("sound/winner.wav") #L'effet sonore avant l'apparition d'un gros avion ennemi
big_enemy.set_volume(0.1)
big_die = pygame.mixer.Sound("sound/big_die.wav") #L'effet sonore du gros avion ennemi détruit
big_die.set_volume(0.2)
up_level = pygame.mixer.Sound("sound/up_level.wav") #Effets sonores lorsque la difficulté est augmentée
up_level.set_volume(0.2)
bomb = pygame.mixer.Sound("sound/bomb.wav") #Le bruit d'une bombe qui explose
bomb.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav") #Le bruit de l'arrivée des ravitaillements
supply_sound.set_volume(0.2)
get_supply = pygame.mixer.Sound("sound/get_supply.wav") #L'effet sonore de se ravitailler
get_supply.set_volume(0.2)
menu_sound = pygame.mixer.Sound("sound/mune.wav") #Effet sonore lorsque le menu est sélectionné
menu_sound.set_volume(0.2)

def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)

def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)

# Accélérer les avions ennemis
def inc_speed(target, inc):
    for each in target:
        each.speed += inc

#Interface "About"
def About():
   
    #image
    about_fun2_img = pygame.image.load("image/about_fun2.png")
    about_fun2_rect = about_fun2_img.get_rect()

    #Bouton de retour
    comeback1_img = pygame.image.load("image/comeback1.png").convert_alpha()#Bouton de retour
    comeback2_img = pygame.image.load("image/comeback2.png").convert_alpha()
    comeback_img = comeback1_img #Définir l'image par défaut
    comeback_rect = comeback1_img.get_rect()
    comeback_rect.left, comeback_rect.top = 901 - 100, 897 - 100
    
    about_font = pygame.font.Font("font/font.TTF", 35)
    Author_text = about_font.render("Auteur: Haicheng WANG, Zongrui XUE", True, WHITE)
    Author_text1 = about_font.render("Mc Neil TEFOGHA TEULONG", True, WHITE)
    Email_text = about_font.render("E-mail: haicheng.wang@efrei.net", True, WHITE)
    Email_text1 = about_font.render("zongrui.xue@efrei.net", True, WHITE)
    Email_text2 = about_font.render("mc-neil.tefogha-teulong@efrei.net", True, WHITE)
    Language_text = about_font.render("Langage: Python", True, WHITE)
    Bgm_text = about_font.render("Bgm: 《Into The Battlefield》", True, WHITE)
   
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                #Bouton de retour
                if comeback_rect.collidepoint(event.pos):
                    comeback_img = comeback1_img
                else:
                    comeback_img = comeback2_img

            elif event.type == MOUSEBUTTONDOWN:
                #collidepoint(event.pos), détecte automatiquement si la souris reste en position, et renvoie True si c'est le cas
                if event.button == 1 and comeback_rect.collidepoint(event.pos):
                    menu_sound.play()
                    Menu()
                
        screen.blit(background, (0, 0))
        screen.blit(about_fun2_img, about_fun2_rect)
        screen.blit(comeback_img, comeback_rect)
        screen.blit(Author_text, (10, 90))
        screen.blit(Author_text1, (10, 140))
        screen.blit(Email_text, (10, 210))
        screen.blit(Email_text1, (10, 260))
        screen.blit(Email_text2, (10, 310))
        screen.blit(Language_text, (10, 380))
        screen.blit(Bgm_text, (10, 450))
      
        
        pygame.display.flip()

        clock.tick(60)

#interface "help"
def Help():
    #Image de fond
    help_fun_img = pygame.image.load("image/help_fun.jpg")
    help_fun_rect = help_fun_img.get_rect()
    #Bouton de retour
    comeback1_img = pygame.image.load("image/comeback1.png").convert_alpha()#Bouton de retour
    comeback2_img = pygame.image.load("image/comeback2.png").convert_alpha()
    comeback_img = comeback1_img #Définir l'image par défaut
    comeback_rect = comeback1_img.get_rect()
    comeback_rect.left, comeback_rect.top = 901 - 100, 897 - 100

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                #Bouton de retour
                if comeback_rect.collidepoint(event.pos):
                    comeback_img = comeback1_img
                else:
                    comeback_img = comeback2_img

            elif event.type == MOUSEBUTTONDOWN:
                #collidepoint(event.pos), détecte automatiquement si la souris reste en position, et renvoie True si c'est le cas
                if event.button == 1 and comeback_rect.collidepoint(event.pos):
                    menu_sound.play()
                    Menu()

        screen.blit(background, (0, 0))
        screen.blit(help_fun_img, (0, 0))
        screen.blit(comeback_img, comeback_rect)

        pygame.display.flip()

        clock.tick(60)

#L'interface principale
def Menu():
    #image1
    menu_fan_img = pygame.image.load("image/menu_fun.png").convert_alpha()#image
    menu_fan_rect = menu_fan_img.get_rect()
    menu_fan_rect.left, menu_fan_rect.top = 0, 0
    #image2
    menu_fan2_img = pygame.image.load("image/menu_fun2.png").convert_alpha()#image
    menu_fan2_rect = menu_fan2_img.get_rect()
    menu_fan2_rect.left, menu_fan2_rect.top = 901 - menu_fan2_rect.width, 0
    
    #Bouton jouer
    begin_game1_img = pygame.image.load("image/begin_game1.png").convert_alpha()#Bouton jouer
    begin_game2_img = pygame.image.load("image/begin_game2.png").convert_alpha()
    begin_game_img = begin_game1_img
    begin_game_rect = begin_game1_img.get_rect()
    begin_game_rect.left, begin_game_rect.top = 264 + 350, 486 - 200

    #bouton d'aide
    help1_img = pygame.image.load("image/help1.png").convert_alpha()#bouton d'aide
    help2_img = pygame.image.load("image/help2.png").convert_alpha()
    help_img = help1_img
    help_rect = help1_img.get_rect()
    help_rect.left, help_rect.top = 264 + 350, 424 + 0

    #Bouton about
    about1_img = pygame.image.load("image/about1.png").convert_alpha()#Bouton about
    about2_img = pygame.image.load("image/about2.png").convert_alpha()
    about_img = about1_img
    about_rect = about1_img.get_rect()
    about_rect.left, about_rect.top = 264 + 350, 424 + 140

    #Effet sonore du bouton de déverrouillage de la souris
    is_sound = True
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #Détecter si la souris est déplacée vers le bouton de pause du jeu
            elif event.type == MOUSEMOTION:
                #Bouton jouer
                if begin_game_rect.collidepoint(event.pos):
                    begin_game_img = begin_game2_img
                else:
                    begin_game_img = begin_game1_img
                #bouton d'aide
                if help_rect.collidepoint(event.pos):
                    help_img = help1_img
                else:
                    help_img = help2_img
                #Bouton about
                if about_rect.collidepoint(event.pos):
                    about_img = about1_img
                else:
                    about_img = about2_img

            elif event.type == MOUSEBUTTONDOWN:
                #collidepoint(event.pos), détecte automatiquement si la souris reste en position, et renvoie True si c'est le cas
                if event.button == 1 and about_rect.collidepoint(event.pos):
                    menu_sound.play()
                    About()
                elif event.button == 1 and begin_game_rect.collidepoint(event.pos):
                    menu_sound.play()
                    main()
                elif event.button == 1 and help_rect.collidepoint(event.pos):
                    menu_sound.play()
                    Help()
                
        screen.blit(background, (0, 0))
        screen.blit(menu_fan2_img, menu_fan2_rect)
        screen.blit(menu_fan_img, (0, 0))
        screen.blit(begin_game_img, begin_game_rect)
        screen.blit(help_img, help_rect)
        screen.blit(about_img, about_rect)
        
        pygame.display.flip()

        clock.tick(60)

def main():
    #pygame.mixer.music.play (nombre de répétitions, heure de début), où le nombre de répétitions sera ajouté à celui d'origine, 
    # si l'heure de début est 1.0, cela signifie que la musique commencera à jouer à partir de la deuxième seconde.
    pygame.mixer.music.play(-1) #Ici, le réglage -1 signifie une boucle infinie

    #Générer nos avions
    me = MyPlane.MyPlane(bg_size)
    # générer des avions ennemis
    enemies = pygame.sprite.Group()#建立一个组

    # Faire apparaître de petits avions ennemis
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 15)
    # Faire apparaître des avions moyens ennemis
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 4)
    # générer de gros avions ennemis
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 2)
    

    # générer des balles
    bullet1 = []
    bullet1_index = 0# pour l'indexation
    BULLET1_MUN = 6#6 balles
    for i in range(BULLET1_MUN):
        bullet1.append(bullet.Bullet1(me.rect.midtop))

    #munitions améliorées
    bullet2 = []
    bullet2_index = 0# pour l'indexation
    BULLET2_MUN = 12#12 balles
    for i in range(BULLET2_MUN // 2):
        bullet2.append(bullet.Bullet2((me.rect.centerx - 33, me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx + 30, me.rect.centery)))

    #index d'image lorsque le joueur est touché par un ennemi
    e1_des_index = 0
    e2_des_index = 0
    e3_des_index = 0
    me_des_index = 0

    #Score statistique
    score = 0
    score_font = pygame.font.Font("font/font.TTF", 36)#définir la police

    #signaler s'il faut mettre le jeu en pause
    paused = False
    #charger l'image de pause
    stopping_img = pygame.image.load("image/stopping.png").convert_alpha()
    stopping_rect = stopping_img.get_rect()
    stopping_rect.left, stopping_rect.top = width / 2 - stopping_rect.width / 2, height / 2 - stopping_rect.height / 2
    stop1_img = pygame.image.load("image/stop1.png").convert_alpha()
    stop2_img = pygame.image.load("image/stop2.png").convert_alpha()
    begin1_img = pygame.image.load("image/begin1.png").convert_alpha()
    begin2_img = pygame.image.load("image/begin2.png").convert_alpha()
    stop_rect = stop1_img.get_rect()
    begin_rect = begin1_img.get_rect()
    paused_rect = stop1_img.get_rect()
    stop_rect.left, stop_rect.top = width - stop_rect.width - 10, 10
    begin_rect.left, begin_rect.top = width - begin_rect.width - 10, 10
    pause_img = stop1_img#définir l'image par défaut

    #Définissez le niveau de difficulté, la difficulté par défaut est 1
    level = 1

    #bombe plein écran
    bomb_img = pygame.image.load("image/boom.jpg").convert_alpha()
    bomb_rect = bomb_img.get_rect()
    bomb_font = pygame.font.Font("font/font.TTF", 48)
    bomb_num = 3#nombre de bombes

    #Donne un approvisionnement toutes les 30 secondes
    bullet_supply = supply.Bullet_Supply(bg_size)
    bomb_supply = supply.Bomb_Supply(bg_size)
    #minuteur
    SUPPLY_TIME = USEREVENT
    pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)

    #Minuteur pour l'amélioration des munitions
    DOUBLE_BULLET_TIME = USEREVENT + 1
    #Indiquer si des munitions renforcées sont utilisées
    is_double_bullet = False

    #Nombre de vies
    life_img = pygame.image.load("image/life.png").convert_alpha()
    life_rect = life_img.get_rect()
    life_num = 3
    
    running = True
    switch_image = True#Changement d'image d'avion
    delay = 100 #délai d'intervention manuelle

    #Annuler la minuterie de notre état d'invincibilité
    INVINCIBLE_TIME = USEREVENT + 2

    #Pour l'ouverture répétée de fichiers
    record_file = False

    #Pour l'écran de fin de partie
    gameover_font = pygame.font.Font("font/font.TTF", 48)
    gameover_font1 = pygame.font.Font("font/font.TTF", 35)
    again_img = pygame.image.load("image/again.png").convert_alpha()#Bouton "une fois de plus
    again_rect = again_img.get_rect()
    gameover_img = pygame.image.load("image/gameover.png").convert_alpha()#Bouton de fin de jeu
    gameover_rect = gameover_img.get_rect()
    again_rect.left, again_rect.top = 318, 424 + 180
    gameover_rect.left, gameover_rect.top = 318, 424 + 300

    #Vérifier si le score dépasse le meilleur score historique
    is_congratulate = False

    #Bouton de retour au menu principal
    comeback1_img = pygame.image.load("image/comeback1.png").convert_alpha()#Bouton de retour
    comeback2_img = pygame.image.load("image/comeback2.png").convert_alpha()
    comeback_img = comeback1_img#Définir l'image par défaut
    comeback_rect = comeback1_img.get_rect()
    comeback_rect.left, comeback_rect.top = 901 - 100, 897 - 100

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #Détecte si le joueur a appuyé sur le bouton pause
            elif event.type == MOUSEBUTTONDOWN:
                if life_num:
                    #collidepoint(event.pos), détecte automatiquement si la souris est à l'intérieur de pos, si oui alors retourne True
                    if event.button == 1 and paused_rect.collidepoint(event.pos):
                        paused = not paused
                        if paused:
                            pygame.time.set_timer(SUPPLY_TIME, 0)#Pause du minuteur
                            pygame.mixer.music.pause()#Musique de fond en pause
                            pygame.mixer.pause()#Tous les autres effets musicaux sont mis en pause
                        else:
                            pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)#Démarrage du minuteur
                            pygame.mixer.music.unpause()#La musique de fond commence
                            pygame.mixer.unpause()#Tous les autres effets musicaux démarrent

                        
                if life_num == 0:
                    
                    #Détecte si le joueur a appuyé sur le bouton Quitter le jeu
                    if event.button == 1 and gameover_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

                    elif event.button == 1 and again_rect.collidepoint(event.pos):
                        main()

                    elif event.button == 1 and comeback_rect.collidepoint(event.pos):
                        menu_sound.play()
                        Menu()
                    

            #Détecte si la souris se déplace vers le bouton de pause du jeu
            elif event.type == MOUSEMOTION:
                if life_num == 0:
                    if event.type == MOUSEMOTION:
                            if comeback_rect.collidepoint(event.pos):
                                comeback_img = comeback1_img
                            else:
                                comeback_img = comeback2_img
                else:
                    if paused_rect.collidepoint(event.pos):
                        if paused:
                            pause_img = begin2_img
                            paused_rect = begin_rect
                        else:
                            pause_img = stop2_img
                            paused_rect = stop_rect
                    else:
                        if paused:
                            pause_img = begin1_img
                            paused_rect = begin_rect
                        else:
                            pause_img = stop1_img
                            paused_rect = stop_rect

            #Détonation de la bombe
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        bomb.play()
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False

            #Délivrance d'un réapprovisionnement à des moments précis
            elif event.type == SUPPLY_TIME:
                supply_sound.play()
                if choice([False, True]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
                    
            #Détection de la durée d'utilisation des munitions améliorées
            elif event.type == DOUBLE_BULLET_TIME:
                is_double_bullet = False
                pygame.time.set_timer(DOUBLE_BULLET_TIME, 0)#Désactiver le minuteur
            #Le temps de l'invincibilité
            elif event.type == INVINCIBLE_TIME:
                me.invincible = False
                pygame.time.set_timer(INVINCIBLE_TIME, 0)

        #Difficulté croissante en fonction du score du joueur
        #Passage à la difficulté 2
        if level == 1 and score >= 300:
            level = 2
            up_level.play()
            #Ajouter 3 petits avions ennemis, 2 avions ennemis moyens et 1 grand avion ennemi
            add_small_enemies(small_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
            #Augmenter la vitesse des avions ennemis
            inc_speed(small_enemies, 1)
        #Passage à la difficulté 3
        elif level == 2 and score >= 800:
            level = 3
            up_level.play()
            #Ajouter 5 petits avions ennemis, 3 avions ennemis moyens et 1 grand avion ennemi
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 1)
            #Augmenter la vitesse des avions ennemis
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        #Passer à la difficulté 4
        elif level == 3 and score >= 1500:
            level = 4
            up_level.play()
            #Ajouter 5 petits avions ennemis, 3 avions ennemis moyens et 2 grands avions ennemis
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            #Augmenter la vitesse des avions ennemis
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
            inc_speed(big_enemies, 1)
        #Passer à la difficulté 5
        elif level == 4 and score >= 2500:
            level = 5
            up_level.play()
            #Ajouter 5 petits avions ennemis, 3 avions ennemis moyens et 2 grands avions ennemis
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            #Augmenter la vitesse des avions ennemis
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
            inc_speed(big_enemies, 1)
        
        screen.blit(background,(0,0))#Afficher l'arrière-plan
        
        if paused:
            #Afficher l'interface en cas de pause
            screen.blit(stopping_img, stopping_rect)
            screen.blit(pause_img, paused_rect)
            #Afficher le score, True indique l'absence d'aliasing
            score_text = score_font.render("Score : %s" % str(score), True, WHITE)
            screen.blit(score_text, (10, 5))#Afficher le score dans le coin supérieur gauche de la page

        if life_num and not paused:
            #Détection des événements clavier
            key_pressed = pygame.key.get_pressed()#Valeur booléenne qui englobe tous les événements clavier

            #Déplacement des avions
            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()

            #Tracer les approvisionnements en bombes et détecter si les joueurs obtiennent des approvisionnements
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, me):#Détecter si notre avion entre en collision avec la partie non transparente de l'approvisionnement
                    get_supply.play()
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False

            #Tracer le réapprovisionnement des balles et détecter si le joueur a été réapprovisionné
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply, me):#Détecter si notre avion entre en collision avec la partie non transparente de l'approvisionnement
                    bullet_supply.active = False
                    get_supply.play()
                    is_double_bullet = True
                    pygame.time.set_timer(DOUBLE_BULLET_TIME, 18 * 1000)
                
                
            #Tirer des balles
            if not(delay % 10):
                #Jouer le bruit d'une balle
                if is_double_bullet:
                    bullets = bullet2
                    bullets[bullet2_index].reset((me.rect.centerx - 33, me.rect.centery))
                    bullets[bullet2_index + 1].reset((me.rect.centerx + 30, me.rect.centery))
                    bullet2_index = (bullet2_index + 2) % BULLET2_MUN
                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset(me.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % BULLET1_MUN

            #Détecte si une balle a touché un avion ennemi
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            e.hit = True
                            e.energy -= 1
                            if e in mid_enemies or big_enemies:
                                if not e.energy:
                                    e.active = False
                            else:
                                e.active = False
            
            #Dessiner des avions ennemis de grande taille
            for each in big_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        #Dessin d'une frappe
                        screen.blit(each.image_hit, each.rect)
                        each.hit= False
                    else:
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)

                    #Dessiner une jauge de santé
                    pygame.draw.line(screen, BLACK, (each.rect.left ,each.rect.top - 5),(each.rect.right, each.rect.top - 5), 2)
                    #Affiche une barre de sang verte lorsque la durée de vie est supérieure à 30 %, sinon elle est rouge.
                    energy_remain = each.energy / enemy.BigEnemy.energy
                    if energy_remain > 0.3:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5),
                                     2)
                    
                    #Effets sonores à venir apparaissant à l'écran
                    if each.rect.bottom == -50:
                        big_enemy.play(-1)
                else:
                    #Destruction
                    if not(delay % 3):
                        if e3_des_index == 0:
                            big_die.play()#Jouer les effets sonores de la mort
                        screen.blit(each.destroy_images[e3_des_index], each.rect)
                        e3_des_index = (e3_des_index + 1) % 6
                        if e3_des_index == 0:
                            big_enemy.stop()
                            score += 100
                            each.reset()
                        

            #Dessiner des avions ennemis de taille moyenne
            for each in mid_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        #Dessin d'une frappe
                        screen.blit(each.image_hit, each.rect)
                        each.hit= False
                    else:
                        screen.blit(each.image, each.rect)

                    #Dessiner une jauge de santé
                    pygame.draw.line(screen, BLACK, (each.rect.left ,each.rect.top - 5),(each.rect.right, each.rect.top - 5), 2)
                    #Lorsque la durée de vie est supérieure à 30%, il s'affichera en vert, sinon il s'affichera en rouge
                    energy_remain = each.energy / enemy.MidEnemy.energy
                    if energy_remain > 0.3:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5),
                                     2)
                    
                else:
                    #Destruction
                    if not(delay % 3):
                        if e2_des_index == 0:
                            big_die.play()#Jouer les effets sonores de la mort
                        screen.blit(each.destroy_images[e2_des_index], each.rect)
                        e2_des_index = (e2_des_index + 1) % 4
                        if e2_des_index == 0:
                            score += 60
                            each.reset()

            #Dessiner un petit avion ennemi
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    #Destruction
                    #big_die.play() #Joue le son de la mort
                    if not(delay % 3):
                        screen.blit(each.destroy_images[e1_des_index], each.rect)
                        e1_des_index = (e1_des_index + 1) % 4
                        if e1_des_index == 0:
                            score += 10
                            each.reset()

            #Détecte si notre avion a été touché et personnalise le type de collision.
            enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
            if enemies_down and not me.invincible:
                me.active = False
                for e in enemies_down:
                    e.active = False
            
            #Dessiner notre avion
            if me.active:
                screen.blit(me.image, me.rect)
            else:
                #Destruction
                #big_die.play() #Joue le son de la mort
                if not(delay % 3):
                    if me_des_index == 0:
                        big_die.play()
                    screen.blit(me.destroy_images[me_des_index], me.rect)
                    me_des_index = (me_des_index + 1) % 5
                    if me_des_index == 0:
                        life_num -= 1
                        me.reset()
                        pygame.time.set_timer(INVINCIBLE_TIME, 3 * 1000)

            #Tracer le nombre de bombes restantes
            bomb_text = bomb_font.render("x %d" % bomb_num, True, WHITE)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_img, (10, height - 10 - bomb_rect.height))
            screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))

            #Tracer le nombre de vies
            if life_num:
                for i in range(life_num):
                    screen.blit(life_img, (width - 10 - (i + 1)*life_rect.width, height - 10 - life_rect.height))

            #Afficher le score, True indique l'absence d'aliasing
            score_text = score_font.render("Score : %s" % str(score), True, WHITE)
            screen.blit(score_text, (10, 5))#Afficher le score dans le coin supérieur gauche de la page

            #Dessiner le bouton pause
            #print(paused_rect)
            screen.blit(pause_img, (797, 10))

            #Contrôler le délai de changement d'image
            if not(delay % 5):
                switch_image = not switch_image

            delay -= 1
            if not delay:
                delay = 100

        #Dessiner l'écran de fin de jeu
        elif life_num == 0:
            #La musique de fond s'arrête
            pygame.mixer.music.stop()
            #arrêter tous les effets sonores
            pygame.mixer.stop()
            #Cesser de distribuer des fournitures
            pygame.time.set_timer(SUPPLY_TIME, 0)

        
            if not record_file:
                record_file = True
                #Lire l'historique des meilleurs scores
                with open("record.txt", "r") as f:
                    record_score = int(f.read())
                if score > record_score:
                    img_num = randint(1, 322)
                    #img_num1 = "image2/" + str(img_num) + ".jpg"
                    #print(img_num1)
                   # with open(img_num1,"rb") as g:
                      #  img_data = g.read()
                    #with open("img_num1.jpg", "wb") as g:
                        #g.write(img_data)
                    score_best = gameover_font.render("Best Score: %s" % str(score), True, WHITE)
                    congratulate = gameover_font1.render("Congratulations on your record!", True, WHITE)
                    is_congratulate = True #Indiquer si le score dépasse le meilleur score historique
                    con_rect = congratulate.get_rect()
                    con_rect.left, con_rect.top = 264 - 50, 486 - 200
                    #print(con_rect.left, con_rect.top)264 486
                    #enregistrer score dans un fichier
                    with open("record.txt", "w") as f:
                        f.write(str(score))
                else:
                    score_best = gameover_font.render("Best Score: %s" % str(record_score), True, WHITE)
                gameover_text = gameover_font.render("GAME OVER!" ,True, WHITE)
                gameover_text_rect = gameover_text.get_rect()
                gameover_text_rect.left, gameover_text_rect.top = 318, 424
            #print(gameover_text_rect.left, gameover_text_rect.top)318 424
            your_score = gameover_font.render("Your Score: %s" % str(score), True, WHITE)
            #Dessiner l'écran de fin de partie
            if is_congratulate:
                screen.blit(congratulate, con_rect)
            screen.blit(again_img, again_rect)
            screen.blit(gameover_img, gameover_rect)
            screen.blit(score_best,(20,20))
            screen.blit(your_score,(20,80))
            screen.blit(gameover_text, gameover_text_rect)
            screen.blit(comeback_img, comeback_rect)

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    try:
        Menu()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
