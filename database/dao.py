from database.DB_connect import DBConnect
from model.neighbors import Neighbor
from model.sighting import Sighting
from model.state import State


class DAO:
    @staticmethod
    def read_all_states():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM state """

        cursor.execute(query)

        for row in cursor:
            result.append(State(**row))


        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_all_neighbors():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM neighbor """

        cursor.execute(query)

        for row in cursor:
            result.append(Neighbor(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_all_sightings():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM sighting """

        cursor.execute(query)

        for row in cursor:
            result.append(Sighting(**row))

        cursor.close()
        conn.close()
        return result