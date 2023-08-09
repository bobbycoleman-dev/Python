# import the function that will return an instance of a connection
from users_app.config.mysql_connection import connect_to_mysql

DATABASE = "users_schema"


# model the class after the friend table from our database
class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # Get info of one user
    @classmethod
    def get_one(cls, id):
        query = """
                SELECT * FROM users
                WHERE id = %(id)s;
                """
        data = {"id": id}
        results = connect_to_mysql(DATABASE).query_db(query, data)
        return User(results[0])

    # Get info for all users
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connect_to_mysql(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append(User(user))
        return users

    # Insert a new user into the db
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO users ( first_name, last_name, email) 
                VALUES ( %(fname)s, %(lname)s, %(email)s);
                """
        results = connect_to_mysql(DATABASE).query_db(query, data)
        return results

    # Update a users information
    @classmethod
    def update(cls, data):
        query = """
                UPDATE users 
                SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s
                WHERE id = %(id)s;
                """
        results = connect_to_mysql(DATABASE).query_db(query, data)
        return results

    # Delete a user from teh db
    @classmethod
    def delete(cls, id):
        query = """
                DELETE FROM users
                WHERE id = %(id)s;
                """
        data = {"id": id}
        results = connect_to_mysql(DATABASE).query_db(query, data)
        return results
