import pygame
import random
import time

# --- inizializzazione di pygame ---
pygame.init()
LARGHEZZA, ALTEZZA = 800, 600
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Cerchi dinamici")

# --- lista di posizioni iniziali (x, y) dei centri dei cerchi ---
cerchi = [
    [100, 100],
    [200, 300],
    [400, 150],
    [600, 400],
    [700, 250]
]

# --- lista dei colori ---
colori = [
    (0, 0, 255),
    (255, 0, 0),
    (0, 255, 0),
    (255, 165, 0),
    (128, 0, 128)
]

# --- velocità dei cerchi (dx, dy) ---
velocita = [[1, 1] for _ in cerchi]

# --- funzione per disegnare i cerchi ---
def disegna_cerchi(lista_pos):
    for i, pos in enumerate(lista_pos):
        pygame.draw.circle(schermo, colori[i], pos, 30)

# --- funzione per aggiornare le posizioni con rimbalzo ---
def aggiorna(lista_pos, velocita):
    for i, pos in enumerate(lista_pos):
        pos[0] += velocita[i][0]
        #pos[1] += velocita[i][1]

        # controllo bordo orizzontale
        if pos[0] < 0 or pos[0] > LARGHEZZA:
            velocita[i][0] *= -1
        # controllo bordo verticale
        if pos[1] < 0 or pos[1] > ALTEZZA:
            velocita[i][1] *= -1

# --- ciclo principale ---
clock = pygame.time.Clock()
running = True
ultimo_cambio = time.time()

while running:
    # gestisce eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # rimuovi un cerchio a caso
                if len(cerchi) > 1:
                    idx = random.randint(0, len(cerchi)-1)
                    cerchi.pop(idx)
                    velocita.pop(idx)
                    colori.pop(idx)
                else:
                    running = False
            elif event.key == pygame.K_a:  # aggiungi un cerchio casuale
                x = random.randint(0, LARGHEZZA)
                y = random.randint(0, ALTEZZA)
                cerchi.append([x, y])
                #velocita.append([random.choice([-1,1]), random.choice([-1,1])])
                velocita.append([random.choice([-1,1]), 0])
                colori.append((random.randint(0,255), random.randint(0,255), random.randint(0,255)))

    # cambia colore dei cerchi ogni secondo
    if time.time() - ultimo_cambio > 1:
        for i in range(len(colori)):
            colori[i] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        ultimo_cambio = time.time()

    # logica del gioco
    aggiorna(cerchi, velocita)

    # disegno sullo schermo
    schermo.fill((255, 255, 255))  # sfondo bianco
    disegna_cerchi(cerchi)
    pygame.display.flip()  # aggiorna tutto lo schermo

    # velocità di aggiornamento (frame al secondo)
    clock.tick(60)

pygame.quit()
