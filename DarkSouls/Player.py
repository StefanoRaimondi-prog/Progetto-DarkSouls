from abc import ABC, abstractmethod
import time


class Personaggio(ABC):
    def __init__(self, nome, salute, stamina):
        self.nome = nome
        self.salute = salute
        self.stamina = stamina
        

    @abstractmethod
    def attacca(self, nemico):
        pass

    @abstractmethod
    def ricevi_danno(self, danno):
        pass


class Giocatore(Personaggio):
    def __init__(self, nome, salute, stamina, attacco, difesa):
        super().__init__(nome, salute, stamina)
        self.attacco_base = attacco
        self.difesa = difesa
        self.numeroNemici = 0
        self.salute_max = salute
        self.stamina_max = stamina

    def attacco_leggero(self, nemico):
        if self.stamina >= 5:
            danno = self.attacco_base
            self.stamina -= 5
            print(f"{self.nome} esegue un attacco leggero contro {nemico.nome}")
            nemico.enemy_ricevi_danno(danno)
        else:
            print(f"{self.nome} non ha abbastanza stamina per un attacco leggero!")

    def attacco_pesante(self, nemico):
        if self.stamina >= 10:
            danno = self.attacco_base * 1.5
            self.stamina -= 10
            print(f"{self.nome} esegue un attacco pesante contro {nemico.nome}")
            nemico.enemy_ricevi_danno(int(danno))
        else:
            print(f"{self.nome} non ha abbastanza stamina per un attacco pesante!")

    def attacca(self, nemico):
        scelta = input("Scegli tipo di attacco - leggero (l) o pesante (p): ").lower()
        print("")#print di puliza
        if scelta == "l":
            self.attacco_leggero(nemico)
        elif scelta == "p":
            self.attacco_pesante(nemico)
        else:
            print("Tipo di attacco non valido. Turno sprecato!")

    def ricevi_danno(self, danno):
        danno_effettivo = max(danno - self.difesa, 0)
        self.salute -= danno_effettivo
        print(f"{self.nome} ha ricevuto {danno_effettivo} danni. Salute rimasta: {self.salute}")


class NPC:
    def __init__(self, nome, dialoghi):
        self.nome = nome
        self.dialoghi = dialoghi

    def parla(self):
        for linea in self.dialoghi:
            input(f"{self.nome}: {linea} (premi invio)")
            time.sleep(1)


# Classe placeholder per Nemico (verrà gestita da un compagno)
class Nemico(Personaggio):
    def __init__(self, nome, salute, stamina, attacco):
        super().__init__(nome, salute, stamina)
        self.attacco_base = attacco

    def attacca(self, nemico):
        print(f"{self.nome} attacca {nemico.nome}")
        nemico.ricevi_danno(self.attacco_base)

    def ricevi_danno(self, danno):
        self.salute -= danno
        print(f"{self.nome} ha subito {danno} danni. Salute rimanente: {self.salute}")
