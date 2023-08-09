from flask_app.config.mysql_connection import connect_to_mysql
from flask_app.models.ninja import Ninja

DATABASE = "dojos_and_ninjas_schema"


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.ninjas = []

    # Insert a new dojo
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO dojos ( name )
                VALUES ( %(dojo_name)s );
                """
        results = connect_to_mysql(DATABASE).query_db(query, data)
        return results

    # Get single dojo info
    @classmethod
    def get_one(cls, dojos_id):
        query = """
                SELECT * FROM dojos
                LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
                WHERE dojos.id = %(dojos_id)s;
                """
        data = {"dojos_id": dojos_id}
        results = connect_to_mysql(DATABASE).query_db(query, data)
        dojo = Dojo(results[0])

        for row in results:
            ninja_data = {
                "id": row["ninjas.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "dojo_id": row["dojo_id"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
            }
            dojo.ninjas.append(Ninja(ninja_data))
        print(ninja_data)
        return dojo

    # Get all dojos info
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connect_to_mysql(DATABASE).query_db(query)
        dojos = []
        for dict in results:
            dojos.append(Dojo(dict))
        return dojos
