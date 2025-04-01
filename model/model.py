from database.corso_DAO import corsoDAO
from database.studente_DAO import studenteDAO
from model.corso import Corso


class Model:
    def __init__(self):
        self.arr_studenti = []
        self.DAOc = corsoDAO()
        self.DAOs = studenteDAO()

    def allCorsi(self):
        tutti_corsi = self.DAOc.getAllCorsi()
        return tutti_corsi

    def iscrittiAlCorso(self, codice):
        arr_studenti = self.DAOs.getIscrizioniCorso(codice)
        return arr_studenti

    def tuttiStudenti(self):
        tutti_stud = self.DAOs.getAllStudenti()
        return tutti_stud

    def trovaStudente(self, matr):
        for stud in self.tuttiStudenti():
            if stud.matricola == int(matr):
                print(f"nome {stud.nome}")
                return stud.nome, stud.cognome
        return "", ""

    def corsiStudente(self, matricola):
        arr_corsi_stud = self.DAOc.getCorsiStudente(matricola)
        return arr_corsi_stud








