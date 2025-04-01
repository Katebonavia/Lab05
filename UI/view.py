import flet as ft
import mysql.connector
from oauthlib.uri_validate import query



class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_matricola = None
        self.txt_name = None
        self.txt_cognome = None
        self.btn_cercaIscritti = None
        self._ddCorsi = None
        self.txt_result = None
        self.txt_container = None
        self.txt_out = None
        self.btn_cercaStudente = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        # dropdown for the "seleziona corso"
        self._ddCorsi = ft.Dropdown(label="Selezionare un Corso",
                     hint_text="Seleziona opzione", width= 800,
                     options=[])
        self._controller.getCorsi()

        #button per cercare iscritti
        self.btn_cercaIscritti = ft.ElevatedButton(text="Cerca Iscritti",
                                                   on_click=self._controller.handleIscrittiCorso)
        row1 = ft.Row([self._ddCorsi, self.btn_cercaIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #ROW with some controls
        # text field for the matricola, name, surname
        self.txt_matricola = ft.TextField(
            label="matricola",
            width=300,
            hint_text="Insert a your matricola"
        )
        self.txt_name = ft.TextField(
            label="nome",
            width=300,
            hint_text="Insert your name",
            read_only=True
        )
        self.txt_cognome = ft.TextField(
            label="cognome",
            width=300,
            hint_text="Insert your surname",
            read_only=True
        )
        row0 = ft.Row([self.txt_matricola, self.txt_name, self.txt_cognome],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row0)

        # button cerca studente
        self.btn_cercaStudente = ft.ElevatedButton(text="Cerca Studente",
                                                   on_click=self._controller.handleCercaStudente)
        self.btn_cercaCorsiStud = ft.ElevatedButton(text="Cerca Corsi Studente",
                                                   on_click=self._controller.handleCercaCorsi)
        row3 = ft.Row([self.btn_cercaStudente, self.btn_cercaCorsiStud],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_out = ft.ListView(expand=True, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_out)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()