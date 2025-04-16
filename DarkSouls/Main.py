from Player import NPC
from Enemy import EnemyBase, EnemyMedio, EnemyBoss
from Menu import scegli_classe, combatti, area_tranquilla
import time


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

        nemico = EnemyMedio()  # Puoi sostituire con EnemyBase() o EnemyBoss()
        combatti(giocatore, nemico)

        if giocatore.salute <= 0:
            print("\nSei stato sconfitto. La tua avventura finisce qui...")
            break
        else:
            input("Hai vinto! Premi invio per tornare all'area tranquilla...")


if __name__ == "__main__":
    main()
