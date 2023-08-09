# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL


# model the class after the friend table from our database
class User:
    db = "users_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_one(cls, id):
        query = """
                SELECT * FROM users
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, {"id": id})
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(User.db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO users ( first_name, last_name, email) 
                VALUES ( %(fname)s, %(lname)s, %(email)s);
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def update(cls, data):
        query = """
                UPDATE users 
                SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def delete(cls, id):
        query = """
                DELETE FROM users
                WHERE id = %(id)s;
                """
        data = {"id": id}
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
