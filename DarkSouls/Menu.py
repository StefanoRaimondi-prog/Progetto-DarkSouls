from Player import Giocatore, NPC


def scegli_classe():
    classi = {
        "1": ("Cavaliere", 120, 80, 8, 15),
        "2": ("Ladro", 100, 120, 10, 5),
        "3": ("Mago", 80, 90, 18, 3),
        "4": ("Barbaro", 110, 110, 20, 2),
        "5": ("Paladino", 110, 100, 12, 10)
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
        "Torna quando sarai un gerriero vero."
    
   
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
        azione = input("Vuoi attaccare (a) o scappare (s)? ").lower()
        if azione == "a":
            giocatore.attacca(nemico)
            if nemico.salute > 0:
                nemico.attacca(giocatore)
        elif azione == "s":
            print(f"{giocatore.nome} è scappato!")
            break
        else:
            print("Azione non valida.")
