from dataclasses import dataclass

@dataclass()
class Studente:
    matricola: int
    nome: str
    cognome: str
    CDS: str

    def __eq__(self, other):  # solo sul parametro materia perchè è la chiave
        return self.matricola == other.matricola

    def __hash__(self):
        # return hash((self.materia, self.punteggio, self.lode))
        return hash(self.matricola)

    def __str__(self):
        return f"{self.nome}, {self.cognome} {self.matricola}"