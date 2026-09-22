# ==========================================================
# MYSQL CONNECTION
# ==========================================================

import os

import pymysql.cursors


class MySQLConnection:
    """
    Administra la conexión con una base de datos MySQL.
    """

    def __init__(self, db):
        self.connection = None

        try:
            self.connection = pymysql.connect(
                host=os.getenv("MYSQL_HOST", "localhost"),
                user=os.getenv("MYSQL_USER", "root"),
                password=os.getenv("MYSQL_PASSWORD", "1234"),
                database=db,
                charset="utf8mb4",
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True,
            )
        except Exception as exc:
            print("No se pudo conectar a MySQL:")
            print(exc)

    def query_db(self, query, data=None):
        if self.connection is None:
            if query.strip().lower().startswith("select"):
                return []
            return False

        with self.connection.cursor() as cursor:
            try:
                print("Running Query:")
                print(query)

                cursor.execute(query, data)

                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()

                if query.strip().lower().startswith("insert"):
                    return cursor.lastrowid

                return None

            except Exception as e:
                print("Something went wrong:")
                print(e)
                if query.strip().lower().startswith("select"):
                    return []
                return False

            finally:
                self.connection.close()


def connectToMySQL(db):
    """
    Recibe el nombre de una base de datos y devuelve
    una instancia de MySQLConnection.
    """
    return MySQLConnection(db)
