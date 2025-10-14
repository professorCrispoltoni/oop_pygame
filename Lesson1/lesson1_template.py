import pygame
import random

# --- inizializzazione di pygame ---
pygame.init()
LARGHEZZA, ALTEZZA = 800, 600
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Esercizio: cerchi in movimento")

# --- lista di posizioni iniziali dei cerchi ---
cerchi = [
    # aggiungi qui alcune posizioni iniziali (x, y)
]

# --- lista dei colori ---
colori = [
    # aggiungi qui alcuni colori RGB
]

# --- funzione per disegnare i cerchi ---
def disegna_cerchi(lista_pos):
    """
    Disegna i cerchi sullo schermo.
    Ogni cerchio deve avere il colore corrispondente.
    """
    pass  # TODO: implementa

# --- funzione per aggiornare le posizioni dei cerchi ---
def aggiorna(lista_pos):
    """
    Aggiorna la posizione dei cerchi.
    I cerchi devono muoversi verso destra.
    Se escono dal lato destro, devono ricomparire a sinistra.
    """
    pass  # TODO: implementa

# --- ciclo principale ---
clock = pygame.time.Clock()
running = True

while running:
    # gestione eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # TODO: implementa logica per rimuovere un cerchio
                pass

    # aggiorna logica
    aggiorna(cerchi)

    # disegna sullo schermo
    schermo.fill((255, 255, 255))
    disegna_cerchi(cerchi)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
