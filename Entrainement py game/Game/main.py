import pygame 
pygame.init()

# generer la fenetre 

pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080,720))

# importer le background du jeu 

background = pygame.image.load('assets/bg.jpg')


running = True

# boucle tant que cette condition est vrai
while running:
    #appliquer l'arriere plan
    screen.blit(background, (0, -200))
    #mettre a jour l'écran
    pygame.display.flip()





    # si le joueur ferme cette fenetre 
    for event in pygame.event.get():
        # pour verifier que l'évenement est fermeture de fenetre 
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")