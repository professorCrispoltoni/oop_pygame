import pygame

pygame.init()

# Finestra e clock
win = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

# Colori
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Giocatore
player = pygame.Rect(40, 45, 30, 30)
vel = 4

# Obiettivo
goal = pygame.Rect(1100, 500, 50, 50)  # rettangolo verde

# Muri
walls = [
    pygame.Rect(0, 0, 1200, 20), pygame.Rect(0, 0, 20, 600),
    pygame.Rect(0, 580, 1200, 20), pygame.Rect(1180, 0, 20, 600),
    pygame.Rect(300, 0, 20, 530), pygame.Rect(20, 100, 230, 20),
    pygame.Rect(70, 200, 230, 20), pygame.Rect(20, 300, 230, 20),
    pygame.Rect(70, 400, 230, 20), pygame.Rect(600, 100, 20, 500),
]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Movimento orizzontale con collisione
    if keys[pygame.K_LEFT]:
        player.x -= vel
        for wall in walls:
            if player.colliderect(wall):
                player.x += vel
    if keys[pygame.K_RIGHT]:
        player.x += vel
        for wall in walls:
            if player.colliderect(wall):
                player.x -= vel

    # Movimento verticale con collisione
    if keys[pygame.K_UP]:
        player.y -= vel
        for wall in walls:
            if player.colliderect(wall):
                player.y += vel
    if keys[pygame.K_DOWN]:
        player.y += vel
        for wall in walls:
            if player.colliderect(wall):
                player.y -= vel

    # Controllo vittoria
    if player.colliderect(goal):
        print("Hai vinto!")
        run = False  # termina il gioco

    # Disegna tutto
    win.fill(WHITE)
    pygame.draw.rect(win, RED, player)
    pygame.draw.rect(win, GREEN, goal)
    for wall in walls:
        pygame.draw.rect(win, BLACK, wall)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
