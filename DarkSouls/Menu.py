from Player import Giocatore, NPC
import random

def scegli_classe():
    classi = {
    "1": ("Cavaliere", 450, 90, 40, 30),     # Il tank definitivo
    "2": ("Ladro", 300, 160, 30, 12),        # Velocità pura, ma più robusto ora
    "3": ("Mago", 280, 130, 60, 10),         # Sempre fragile, ma sopravvive a 2 colpi boss
    "4": ("Barbaro", 400, 120, 55, 18),      # Tanta vita e tanti schiaffi
    "5": ("Paladino", 420, 110, 38, 35)      # Resistenza top, equilibrato e tenace
    }

    print("Scegli la tua classe:")
    for chiave, dati in classi.items():
        nome, salute, stamina, attacco, difesa = dati
        print(f"{chiave}) {nome} - Attacco: {attacco}, Difesa: {difesa}, Stamina: {stamina}, Salute: {salute}")

    scelta = input("Inserisci il numero della classe: ")
    if scelta in classi:
        nome, salute, stamina, attacco, difesa = classi[scelta]
        return Giocatore(nome, salute, stamina, attacco, difesa)
    else:
        print("Scelta non valida.")
        return scegli_classe()


def area_tranquilla():
    npc1 = NPC("Maestro Alaric", [
        "Hai molto da imparare, giovane guerriero...",
        "Ogni scelta che fai ti cambia."
    ])

    npc2 = NPC("Mercante Lyra", [
        "Non ho nulla da vendere oggi...",
        "Ma forse domani tornerai con più fortuna."
    ])

    npc3 = NPC("Guerriero Errante", [
        "La battaglia è la mia vita.",
        "Torna quando sarai un guerriero vero."
    ])

    while True:
        print("\n=== Area Tranquilla ===")
        print("1) Parla con Maestro Alaric")
        print("2) Parla con Mercante Lyra")
        print("3) Parla con Guerriero Errante")
        print("4) Esci e affronta il prossimo nemico")

        scelta = input("Cosa vuoi fare? ")

        if scelta == "1":
            npc1.parla()
        elif scelta == "2":
            npc2.parla()
        elif scelta == "3":
            npc3.parla()
        elif scelta == "4":
            print("Ti incammini verso la prossima battaglia...")
            break
        else:
            print("Scelta non valida.")


def combatti(giocatore, nemico):
    while giocatore.salute > 0 and nemico.salute > 0:
        print(f"\n[HUD] {giocatore.nome} - Salute: {giocatore.salute} | Stamina: {giocatore.stamina}")
        print(f"\n[Nemico] {nemico.nome} - Salute: {nemico.salute}")
        azione = input("Vuoi attaccare (a) o scappare (s)? ").lower()
        if azione == "a":
            giocatore.attacca(nemico)
            if nemico.salute > 0:
                if random.randint(1,2) == 1:
                    nemico.enemyAttaccoLeggero(giocatore)
                else:
                    nemico.enemyAttaccoPesante(giocatore)
        elif azione == "s":
            print(f"{giocatore.nome} è scappato!")
            break
        else:
            print("Azione non valida.")
