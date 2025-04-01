import flet as ft
from model import model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def getCorsi(self):
        tuttiCorsi = self._model.allCorsi()
        for row in tuttiCorsi:
            self._view._ddCorsi.options.append(ft.dropdown.Option(key=row.codins, text=row.__str__()))
        return tuttiCorsi

    def handleIscrittiCorso(self, e):

        corso = self._view._ddCorsi.value
        if corso is None or corso == "":
            self._view.create_alert("Selezionare un corso!")
            return
        self._view.txt_out.controls.clear()
        self._view.txt_out.controls.append(ft.Text(f"Codice insegnamento: {corso}"))
        self._view.update_page()

        self._view.txt_out.controls.append(ft.Text(f"Gli iscritti sono: {len(self._model.iscrittiAlCorso(corso))}\n "))

        for stud in  self._model.iscrittiAlCorso(corso):
            self._view.txt_out.controls.append(
                ft.Text(str(stud.__str__()), color="black")
            )
        self._view.update_page()


    def handleCercaStudente(self,e):
        matricola = self._view.txt_matricola.value
        if matricola is None or matricola == "":
            self._view.create_alert("Scrivere una matricola!")
            return
        nome_stud, cognome_stud = self._model.trovaStudente(matricola)
        self._view.txt_name.value = nome_stud
        self._view.txt_cognome.value = cognome_stud
        if nome_stud == "" and cognome_stud == "":
            self._view.create_alert("Matricola non esiste!")
            return
        self._view.update_page()

    def handleCercaCorsi(self,e):
        matricola = self._view.txt_matricola.value
        if matricola is None or matricola == "":
            self._view.create_alert("Selezionare una matricola!")
            return
        self._view.txt_out.controls.clear()
        self._view.txt_out.controls.append(ft.Text(f"Matricola: {matricola}"))
        self._view.update_page()

        self._view.txt_out.controls.append(ft.Text(f"I corsi sono: {len(self._model.corsiStudente(matricola))}\n "))

        for c in  self._model.corsiStudente(matricola):
            self._view.txt_out.controls.append(
                ft.Text(str(c.__str__()), color="black")
            )
        self._view.update_page()







