from Player import NPC
from Enemy import EnemyBase, EnemyMedio, EnemyBoss
from Menu import scegli_classe, combatti, area_tranquilla
import time
import random


def intro_narrativa():
    scene = [
        "...Il fuoco si spegne lentamente...",
        "Un'epoca oscura si avvicina...",
        "Solo il Non Morto prescelto può invertire il destino...",
        "Che sia tu?",
        "O solo un altro rigurgito di follia...",
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
        npc = NPC("Vergine Misteriosa", [
            "Benvenuto, guerriero.",
            "Solo i forti sopravvivono.",
            "Buona fortuna."
        ])
        npc.parla()

        # Combattimento reale con un nemico scelto casualmente
        print("\nStai per affrontare un nemico...")
        time.sleep(1)
        if giocatore.numeroNemici % 3 == 0 and giocatore.numeroNemici > 0: #ogni 3 nemici sconfitti
            nemico = EnemyBoss()
            print("Incontri il boss...")
        else:
            nemico =  EnemyMedio() if random.randint(1,2) == 1 else EnemyBase() 
        combatti(giocatore, nemico)

        if giocatore.salute <= 0:
            print("\nSEI MORTO!")
            break
        else:
            input("Premi invio per tornare all'area tranquilla...")
        if nemico.isBoss and nemico.salute <= 0:
            print("----\nComlimenti hai ottenuto il ricettacolo della conoscenza proibita...")
            print("Si distinguono alcune rune... OOP")
            print("Le rune brillano... \n Un sussuro ti chiede:  \n Riuscira a trovare il Lord?")
            break


if __name__ == "__main__":
    main()
