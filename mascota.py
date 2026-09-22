# ==========================================================
# MODELO MASCOTA
# ==========================================================

from mysqlconnection import connectToMySQL


class Mascota:
    """
    Representa un registro de la tabla mascotas.
    """

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.tipo = data["tipo"]
        self.color = data["color"]
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO mascotas (nombre, tipo, color)
            VALUES (%(nombre)s, %(tipo)s, %(color)s);
        """
        return connectToMySQL("primera_flask").query_db(query, data)

    def update(self):
        query = """
            UPDATE mascotas
            SET nombre = %(nombre)s,
                tipo = %(tipo)s,
                color = %(color)s
            WHERE id = %(id)s;
        """
        data = {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "color": self.color,
        }
        return connectToMySQL("primera_flask").query_db(query, data)

    @classmethod
    def delete(cls, id):
        query = """
            DELETE FROM mascotas
            WHERE id = %(id)s;
        """
        data = {"id": id}
        return connectToMySQL("primera_flask").query_db(query, data)

    @classmethod
    def get_all(cls):
        query = """
            SELECT *
            FROM mascotas
            ORDER BY id DESC;
        """

        resultados = connectToMySQL("primera_flask").query_db(query)

        if not resultados:
            return []

        return [cls(mascota) for mascota in resultados]

    @classmethod
    def get_by_id(cls, id):
        query = """
            SELECT *
            FROM mascotas
            WHERE id = %(id)s;
        """

        data = {"id": id}
        resultados = connectToMySQL("primera_flask").query_db(query, data)

        if not resultados:
            return None

        return cls(resultados[0])
