# 🟢 Lezione: Colpisci i Cerchi

![figura 1](../images/hit_circles.png)

## 🎯 Obiettivi
- Ripassare liste e tuple per memorizzare oggetti
- Usare funzioni per organizzare il codice
- Gestire eventi di mouse e tastiera con Pygame
- Disegnare oggetti con `pygame.draw.circle`

> Premi **SPAZIO** per generare nuovi cerchi e cliccali per guadagnare punti.  
> Se un cerchio tocca il fondo, perdi 1 punto.

---

## 🧩 Istruzioni di lavoro

Apri `template.py` e completa i `# TODO` nelle funzioni principali.

### 1. Disegnare i cerchi
Ogni cerchio è `[x, y, colore, raggio]`. La funzione deve scorrere la lista dei cerchi e disegnarli.

```python
def disegna_cerchi(lista_cerchi):
    """Disegna tutti i cerchi sullo schermo"""
    # TODO: per ogni cerchio nella lista, usa pygame.draw.circle()
