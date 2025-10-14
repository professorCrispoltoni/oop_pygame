import pygame
import random
import time

# --- inizializzazione di pygame ---
pygame.init()
LARGHEZZA, ALTEZZA = 800, 600
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Ripasso: liste, funzioni e cicli")

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

# --- funzione per disegnare i cerchi ---
def disegna_cerchi(lista_pos):
    for i,pos in enumerate(lista_pos):   # uso del ciclo for
        pygame.draw.circle(schermo, colori[i], pos, 30)

# --- funzione per aggiornare le posizioni ---
def aggiorna(lista_pos):
    for pos in lista_pos:
        pos[0] += 1   # sposta ogni cerchio un po’ a destra
        if pos[0] > LARGHEZZA:  # se esce a destra, torna a sinistra
            pos[0] = 0

# --- ciclo principale ---
clock = pygame.time.Clock()
running = True

while running:
    # gestisce eventi (es. chiusura finestra)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # aggiungi un cerchio con spazio
                if len(cerchi)>1:
                    cerchi.pop(-1)
                else:
                    running = False

    # logica del gioco
    aggiorna(cerchi)

    # disegno sullo schermo
    schermo.fill((255, 255, 255))   # sfondo bianco
    disegna_cerchi(cerchi)
    pygame.display.flip()
    
    #time.sleep(1)

    # velocità di aggiornamento (frame al secondo)
    clock.tick(60)

pygame.quit()
