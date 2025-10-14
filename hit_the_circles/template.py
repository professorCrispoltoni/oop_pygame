import pygame
import random
import math

# --- Inizializzazione ---
pygame.init()
LARGHEZZA, ALTEZZA = 600, 400
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Colpisci i cerchi")
clock = pygame.time.Clock()

# --- Variabili ---
punteggio = 0

cerchi = []   # lista di cerchi: [x, y, colore, raggio]


# --- Funzioni ---
def disegna_cerchi(lista_cerchi):
    """Disegna tutti i cerchi"""
    # TODO: ciclo for per disegnare i cerchi con pygame.draw.circle


def muovi_cerchi(lista_cerchi, speed):
    """Aggiorna posizione verticale"""
    global punteggio
    # TODO: far scendere i cerchi
    # TODO: se un cerchio tocca il fondo, riportarlo in alto e togliere 1 punto


def aggiungi_cerchio(lista_cerchi):
    """Aggiunge un nuovo cerchio in alto con valori casuali"""
    # TODO: posizione x casuale tra 0 e LARGHEZZA, y=0
    # TODO: colore casuale
    # TODO: raggio fisso (es. 25)
    # TODO: aggiungerlo alla lista


def clic_su_cerchi(lista, pos_mouse):
    """Controlla se il clic è dentro un cerchio"""
    global punteggio
    # TODO: calcolare distanza mouse-centro
    # TODO: se distanza <= raggio → punteggio +1 e rimuovere il cerchio


# --- Ciclo principale ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clic_su_cerchi(cerchi, event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                aggiungi_cerchio(cerchi)

    muovi_cerchi(cerchi, 2)

    schermo.fill((255,255,255))
    disegna_cerchi(cerchi)

    # Mostra punteggio
    font = pygame.font.SysFont(None, 40)
    testo = font.render(f"Punteggio: {punteggio}", True, (0,0,0))
    schermo.blit(testo, (10,10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
