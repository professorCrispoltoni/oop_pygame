import pygame
 
pygame.init()
 
# Finestra e clock
win = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
 
# Colori
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255,255,255)
 
# Giocatore
player_rect = pygame.Rect(500, 500, 100, 100)
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (40, 40))  # stessa dimensione del Rect
#win.blit(player_img, (player_rect.x, player_rect.y))


player = pygame.Rect(40, 45, 30, 30)
vel = 4
 
# Obiettivo
goal = pygame.Rect(1100, 500, 50, 50)  # rettangolo verde
 
#nemico
nemico1 = pygame.Rect(420, 30, 30,30)
 
nemico2 = pygame.Rect(420, 545, 30,30)
 
nemico3 = pygame.Rect(525, 180, 30,30)
 
velocita = 50
 
# Muri
walls = [
    pygame.Rect(0, 0, 1200, 20), pygame.Rect(0, 0, 20, 600),
    pygame.Rect(0, 580, 1200, 20), pygame.Rect(1180, 0, 20, 600),
    pygame.Rect(100,00,30,350), pygame.Rect(100,430,30,400),
    #primi 2 
    pygame.Rect(200,65, 30,190),pygame.Rect(200,340, 30,190),
    pygame.Rect(450,65, 30,190),pygame.Rect(450,340, 30,190),

    pygame.Rect(200,65, 250,30),pygame.Rect(200,340, 250,30),
    pygame.Rect(200,225, 250,30),pygame.Rect(200,500, 250,30),
    #secondi 2
    pygame.Rect(600,65, 30,190),pygame.Rect(600,340, 30,190),
    pygame.Rect(850,65, 30,190),pygame.Rect(850,340, 30,190),

    pygame.Rect(600,65, 250,30),pygame.Rect(600,340, 250,30),
    pygame.Rect(600,225, 250,30),pygame.Rect(600,500, 250,30),
    pygame.Rect(1000,-200,30,350), pygame.Rect(1000,220,30,400),

 
]
 
dt = clock.tick(60) / 1000.0
 
verso = 1
distanza = 220
startx = nemico1.x
starty = nemico3.y
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #movimento nemico

    #nemico 1
    nemico1.x += verso * velocita * dt
 
    if verso == 1 and nemico1.x >= startx + distanza:
        nemico1.x = startx + distanza
        verso = -1
 
    if verso == -1 and nemico1.x <= startx:
        nemico1.x = startx
        verso = 1
 
 
    #nemico 2
 
    nemico2.x += verso * velocita * dt
 
    if verso == 1 and nemico2.x >= startx + distanza:
        nemico2.x = startx + distanza
        verso = -1
 
    if verso == -1 and nemico2.x <= startx:
        nemico2.x = startx
        verso = 1

    #nemico 3
    nemico3.y += verso * velocita * dt
 
    if verso == 1 and nemico3.y >= starty + distanza:
        nemico3.y = starty + distanza
        verso = -1
 
 
    if verso == -1 and nemico3.y <= starty:
        nemico3.y = starty
        verso = 1


    keys = pygame.key.get_pressed()
    if player.colliderect(nemico1):
        print("Hai perso")
        run = False
    if player.colliderect(nemico2):
        print("Hai perso")
        run = False
 
    if player.colliderect(nemico3):
        print("Hai perso")
        run = False
 
    # Movimento orizzontale con collisione
    if keys[pygame.K_a]:
        player.x -= vel
        for wall in walls:
            if player.colliderect(wall):
                player.x += vel
    if keys[pygame.K_d]:
        player.x += vel
        for wall in walls:
            if player.colliderect(wall):
                player.x -= vel
 
    # Movimento verticale con collisione
    if keys[pygame.K_w]:
        player.y -= vel
        for wall in walls:
            if player.colliderect(wall):
                player.y += vel
    if keys[pygame.K_s]:
        player.y += vel
        for wall in walls:
            if player.colliderect(wall):
                player.y -= vel
 
    # Controllo vittoria
    if player.colliderect(goal):
        print("Hai vinto!")
        run = False  # termina il gioco
 
    # Disegna tutto
    win.fill(BLACK)
    
    pygame.draw.rect(win, YELLOW, player)
    pygame.draw.rect(win, GREEN, goal)
    pygame.draw.rect(win, RED, nemico1)
    pygame.draw.rect(win, RED, nemico2)
    pygame.draw.rect(win, RED, nemico3)
    
    for wall in walls:
        pygame.draw.rect(win, BLUE, wall)
        
    win.blit(player_img, (player_rect.x, player_rect.y))
 
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()