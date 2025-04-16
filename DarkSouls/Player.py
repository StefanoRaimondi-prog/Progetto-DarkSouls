from abc import ABC, abstractmethod

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

    def attacca(self, nemico):
        print(f"{self.nome} attacca {nemico.nome}")
        danno = self.attacco_base
        nemico.ricevi_danno(danno)

    def ricevi_danno(self, danno):
        danno_effettivo = max(danno - self.difesa, 0)
        self.salute -= danno_effettivo
        print(f"{self.nome} ha ricevuto {danno_effettivo} danni. Salute rimasta: {self.salute}")


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


class NPC:
    def __init__(self, nome, dialoghi):
        self.nome = nome
        self.dialoghi = dialoghi

    def parla(self):
        for linea in self.dialoghi:
            input(f"{self.nome}: {linea} (premi invio)")
