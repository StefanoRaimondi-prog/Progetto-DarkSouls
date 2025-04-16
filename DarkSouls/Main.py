from Player import NPC
from enemy import EnemyBase, EnemyMedio, EnemyBoss
from Menu import scegli_classe, combatti, area_tranquilla
import time
import random


def intro_narrativa():
    scene = [
        "...Il fuoco si spegne lentamente...",
        "Un'epoca oscura si avvicina...",
        "Solo pochi prescelti possono invertire il destino...",
        "Tu sei uno di loro."
    ]
    for frase in scene:
        print(frase)
        time.sleep(2)
    print("\n--- INIZIO GIOCO ---\n")


def main():
    intro_narrativa()
    giocatore = scegli_classe()
    print(f"Hai scelto la classe {giocatore.nome}. Preparati al viaggio...\n")

    while True:
        area_tranquilla()

        # Dialogo iniziale
        npc = NPC("Vecchio Saggio", [
            "Benvenuto, guerriero.",
            "Solo i forti sopravvivono.",
            "Buona fortuna."
        ])
        npc.parla()

        # Combattimento reale con un nemico scelto casualmente
        print("\nStai per affrontare un nemico...")
        time.sleep(1)
        print(giocatore.numeroNemici)
        if giocatore.numeroNemici % 3 == 0 and giocatore.numeroNemici > 0: #ogni 3 nemici sconfitti
            nemico = EnemyBoss()
            print("Incontri il boss")
        else:
            nemico =  EnemyMedio() if random.randint(1,2) == 1 else EnemyBase() 
        combatti(giocatore, nemico)

        if giocatore.salute <= 0:
            print("\nSei stato sconfitto. La tua avventura finisce qui...")
            break
        else:
            giocatore.numeroNemici +=1
            giocatore.salute = giocatore.salute_max
            giocatore.stamina = giocatore.stamina_max
            input("Hai vinto! Premi invio per tornare all'area tranquilla...")
            


if __name__ == "__main__":
    main()
