from Player import Giocatore


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
