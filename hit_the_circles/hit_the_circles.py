import pygame
import random
import math

# --- Inizializzazione ---
pygame.init()
LARGHEZZA, ALTEZZA = 600, 400
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Colpisci i cerchi")
clock = pygame.time.Clock()

# Cerchio: [x, y, colore, raggio]
c1 = [300, 200, (0, 0, 255), 25]
c2 = [400, 200, (255, 0, 0), 25]
c3 = [500, 200, (0, 255, 0), 25]
cerchi = [c1,c2,c3]

punteggio = 0

# --- Funzioni ---
def disegna_cerchi(lista_cerchi):
    """Disegna un cerchio sullo schermo"""
    for c in lista_cerchi:
        pygame.draw.circle(schermo, c[2], (c[0], c[1]), c[3])
        
def muovi_cerchi(lista_cerchi, speed):
    global punteggio
    for c in lista_cerchi:
        c[1] += speed  # y = y + velocità
        if c[1] + c[3] > ALTEZZA:  # se tocca il fondo, ricomincia dall'alto
            c[1] = 0
            punteggio -= 1
            print("punteggio: ",punteggio)
            
def aggiungi_cerchio(lista_cerchi):
    """Aggiunge un nuovo cerchio in cima"""
    x = random.randint(0, LARGHEZZA)
    y = 0
    colore = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    lista_cerchi.append([x, y, colore, 25])

def clic_su_cerchi(lista, pos_mouse):
    """Controlla se il clic è dentro un cerchio"""
    global punteggio
    for c in lista:
        distanza = math.sqrt((c[0]-pos_mouse[0])**2 + (c[1]-pos_mouse[1])**2)
        if distanza <= c[3]:
            punteggio += 1
            print("punteggio: ",punteggio)
            lista.remove(c)

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

    muovi_cerchi(cerchi, 1)
    schermo.fill((255,255,255))   # sfondo bianco
    disegna_cerchi(cerchi)      # disegna il cerchio
    
    # Mostra punteggio
    font = pygame.font.SysFont(None, 40)
    testo = font.render(f"Punteggio: {punteggio}", True, (0,0,0))
    schermo.blit(testo, (10,10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
