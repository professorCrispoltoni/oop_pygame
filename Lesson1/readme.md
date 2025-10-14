# Esercizio: Cerchi in movimento

In questo esercizio dovrai completare un programma Pygame che mostra dei cerchi colorati che si muovono verso destra sullo schermo.

## Obiettivi

1. **Disegnare i cerchi**  
   Completa la funzione `disegna_cerchi(lista_pos)` in modo che disegni ogni cerchio nella posizione corretta con il colore corrispondente.

2. **Aggiornare le posizioni**  
   Completa la funzione `aggiorna(lista_pos)` così che ogni cerchio si muova verso destra e ricompaia a sinistra quando esce dallo schermo.

3. **Rimuovere cerchi con la barra spaziatrice**  
   All’interno del ciclo degli eventi, implementa la logica per rimuovere l’ultimo cerchio dalla lista quando si preme `SPACE`.  
   - Se rimane solo un cerchio, il programma deve terminare.

## Suggerimenti

- Usa `pygame.draw.circle()` per disegnare i cerchi.
- Puoi usare un ciclo `for` con `enumerate()` per collegare le posizioni ai colori.
- Controlla le coordinate `x` dei cerchi e riportale a 0 quando superano `LARGHEZZA`.

## Estensioni (facoltativo)

- Aggiungi movimento verticale casuale ai cerchi.
- Cambia colore del cerchio quando rimbalza sul bordo dello schermo.
- Aggiungi più cerchi e gestisci il loro inserimento con un altro tasto.

---

Buon divertimento e buon ripasso di liste, cicli e funzioni in Python!
