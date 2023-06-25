import pygame

class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("image/me.png").convert_alpha()#image de nos avions
        self.destroy_images = []
        self.destroy_images.extend([pygame.image.load("image/me_des_1.png").convert_alpha(), pygame.image.load("image/me_des_2.png").convert_alpha(),\
                                    pygame.image.load("image/me_des_3.png").convert_alpha(),pygame.image.load("image/me_des_4.png").convert_alpha(),\
                                    pygame.image.load("image/me_des_5.png").convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # Où apparaissent nos avions
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height-64
        self.speed = 10# Vitesse de l'avion
        self.active = True #Statut de survie
        self.invincible = False # Définir l'invincibilité
        # Définir un masque pour supprimer la partie transparente de l'objet surfacique lors de la détection des collisions
        self.mask = pygame.mask.from_surface(self.image)

    def moveUp(self):# Bouger en haut
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):#Bouger en bas
        if self.rect.bottom < self.height - 60 :
            self.rect.top += self.speed
        else:
            #self.rect.bottom = self.height
            self.rect.bottom = self.height - 60

    def moveLeft(self):#Bouger à gauche
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):#Bouger à droite
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height-64
        self.active = True
        self.invincible = True
