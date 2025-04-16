from Player import NPC, Nemico
from Menu import scegli_classe, combatti


def main():
    giocatore = scegli_classe()
    print(f"Hai scelto la classe {giocatore.nome}. Preparati al combattimento!")

    # Incontro con NPC
    npc = NPC("Vecchio Saggio", [
        "Benvenuto, guerriero.",
        "Solo i forti sopravvivono.",
        "Buona fortuna."
    ])
    npc.parla()

    # Primo nemico
    nemico = Nemico("Non-morto", 80, 50, 10)
    combatti(giocatore, nemico)


if __name__ == "__main__":
    main()
