import pygame

pygame.init()

# Finestra e clock
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mini Gioco")
clock = pygame.time.Clock()

# Colori
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Giocatore
player = pygame.Rect(50, 250, 40, 40)
vel = 5

# Obiettivo
goal = pygame.Rect(700, 250, 50, 50)

# Due muri con passaggio in mezzo
walls = [
    pygame.Rect(200, 100, 20, 400),  # muro sinistro
]

run = True
font = pygame.font.SysFont(None, 60)
won = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if not won:
        # Movimento orizzontale
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

        # Movimento verticale
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
            won = True

    # Disegna tutto
    win.fill(WHITE)
    pygame.draw.rect(win, RED, player)
    pygame.draw.rect(win, GREEN, goal)
    for wall in walls:
        pygame.draw.rect(win, BLACK, wall)

    # Messaggio vittoria
    if won:
        text = font.render("HAI VINTO!", True, (0, 128, 0))
        win.blit(text, (250, 250))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
