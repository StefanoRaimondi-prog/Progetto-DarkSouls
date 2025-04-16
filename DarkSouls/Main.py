from Player import NPC, Nemico
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

        # Combattimento placeholder (nemici gestiti in seguito)
        print("\n(Nessun nemico reale disponibile - il sistema sarà integrato in seguito.)")
        input("Premi invio per tornare all'area tranquilla...")


if __name__ == "__main__":
    main()
