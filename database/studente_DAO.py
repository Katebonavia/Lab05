# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model import studente


class studenteDAO:

    def getAllStudenti(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select * from studente"""
        cursor.execute(query)
        res = []
        for row in cursor:
            newStudente = studente.Studente(row["matricola"], row["nome"], row["cognome"], row["CDS"])
            res.append(newStudente)
        cnx.close()
        return res

    def getIscrizioniCorso(self, codice):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query =  """select * 
                    from iscrizione i
                    where i.codins = %s """
        cursor.execute(query, (codice,))
        iscritti = []
        studenti_iscr = []
        for row in cursor:
            iscritti.append(row)

        for isc in iscritti:
            for stud in self.getAllStudenti():
                if stud.matricola == isc["matricola"]:
                    studenti_iscr.append(stud)
        cnx.close()
        return studenti_iscr


