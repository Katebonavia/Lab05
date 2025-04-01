# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection, DBConnect
from model import corso, studente
from model.corso import Corso


class corsoDAO:

    def getAllCorsi(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select * from corso"""
        cursor.execute(query)
        res = []
        for row in cursor:
            newCorso = corso.Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
            res.append(newCorso)
        cnx.close()
        cursor.close()
        return res

    def getCorsiStudente(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select * 
                    from iscrizione i
                    where i.matricola = %s """
        cursor.execute(query, (matricola,))
        corsi = []
        corsi_iscr = []
        for row in cursor:
            corsi.append(row)
        for isc in corsi:
            for c in self.getAllCorsi():
                if c.codins==isc["codins"]:
                    corsi_iscr.append(c)
        cnx.close()
        return corsi_iscr