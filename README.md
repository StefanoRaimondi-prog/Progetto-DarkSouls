# ⚔️ Souls-Like Python Game

Un progetto ispirato a **Dark Souls**, sviluppato in **Python** utilizzando la **programmazione a oggetti (OOP)**.  
Il gioco include meccaniche di combattimento, classi giocatore, dialoghi con NPC e nemici con comportamento differenziato.

---

## 🧠 Funzionalità principali

✅ Selezione della classe iniziale (5 classi con statistiche uniche)  
✅ Area tranquilla con NPC interattivi  
✅ Sistema di combattimento con attacchi leggeri e pesanti  
✅ Nemici di difficoltà crescente: base, medio, boss  
✅ Utilizzo di **classi astratte** e principi **OOP**  
✅ Loop continuo tra area sicura e combattimento

---

## 📂 Struttura dei file

```
├── Main.py       # Avvio del gioco e ciclo principale
├── Player.py     # Classi Giocatore, NPC e classe base Personaggio
├── Menu.py       # Menu iniziale, area tranquilla e gestione combattimenti
└── Enemy.py      # Classi nemico: EnemyBase, EnemyMedio, EnemyBoss
```

---

## 🚀 Avvio del gioco

Assicurati di avere **Python 3** installato.  
Per avviare il gioco, esegui il seguente comando da terminale:

```bash
python Main.py
```

---

## 🧙‍♂️ Classi giocabili

| Classe    | Attacco | Difesa | Stamina | Salute |
|-----------|---------|--------|---------|--------|
| Cavaliere |   ✅    |   ✅   |    ✅   |   ✅   |
| Ladro     |   ✅    |        |    ✅   |        |
| Mago      |        |        |    ✅   |        |
| Barbaro   |   ✅    |        |         |   ✅   |
| Paladino  |   ✅    |   ✅   |         |   ✅   |

*Nota: Le statistiche dettagliate sono presenti all’interno del gioco.*

---

## 🔮 Possibili sviluppi futuri

- Sistema di **salvataggio/caricamento**  
- Aggiunta di **oggetti e inventario**  
- **Boss fight finali** con più fasi  
- Espansione delle **interazioni nell’area tranquilla**  
- Meccaniche di **crescita del personaggio**

---

## 👨‍💻 Autori

- Stefano Raimondi  
- Ciro Maresca

