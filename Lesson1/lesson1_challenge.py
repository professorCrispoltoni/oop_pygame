import pygame
import random
import math

# --- inizializzazione di pygame ---
pygame.init()
LARGHEZZA, ALTEZZA = 800, 600
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Ripasso: liste, funzioni e cicli")

# --- lista di posizioni iniziali (x, y) ---
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

# --- lista delle velocità (dx, dy) ---
velocita = [
    [2, 1],
    [3, -2],
    [-2, 2],
    [1, -3],
    [2, -1]
]

RAGGIO = 30

# --- funzione per disegnare i cerchi ---
def disegna_cerchi(lista_pos, lista_col):
    for i, pos in enumerate(lista_pos):
        pygame.draw.circle(schermo, lista_col[i], pos, RAGGIO)

# --- funzione per aggiornare le posizioni ---
def aggiorna(lista_pos, lista_vel):
    for i in range(len(lista_pos)):
        lista_pos[i][0] += lista_vel[i][0]
        lista_pos[i][1] += lista_vel[i][1]

        # --- rimbalzo sui bordi ---
        if lista_pos[i][0] < RAGGIO or lista_pos[i][0] > LARGHEZZA - RAGGIO:
            lista_vel[i][0] = -lista_vel[i][0]
        if lista_pos[i][1] < RAGGIO or lista_pos[i][1] > ALTEZZA - RAGGIO:
            lista_vel[i][1] = -lista_vel[i][1]

# --- funzione per controllare collisioni ---
def controlla_collisioni(lista_pos, lista_vel):
    for i in range(len(lista_pos)):
        for j in range(i+1, len(lista_pos)):
            dx = lista_pos[i][0] - lista_pos[j][0]
            dy = lista_pos[i][1] - lista_pos[j][1]
            distanza = math.sqrt(dx*dx + dy*dy)

            if distanza < 2*RAGGIO:  # collisione
                # rimbalzo semplice: invertiamo direzioni
                print(f"Collisione tra cerchio {i} e cerchio {j}")
                lista_vel[i][0] = -lista_vel[i][0]
                lista_vel[i][1] = -lista_vel[i][1]
                lista_vel[j][0] = -lista_vel[j][0]
                lista_vel[j][1] = -lista_vel[j][1]

# --- ciclo principale ---
clock = pygame.time.Clock()
running = True

while running:
    # gestisce eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # aggiungi un cerchio
                if len(cerchi)>1:
                    cerchi.pop(-1)
                else:
                    running = False

    # logica
    aggiorna(cerchi, velocita)
    controlla_collisioni(cerchi, velocita)

    # disegno
    schermo.fill((255, 255, 255))
    disegna_cerchi(cerchi, colori)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
