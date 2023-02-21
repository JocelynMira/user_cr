from flask_app.config.mysqlconnection import connectToMySQL

# user.py
class User:
    DB = "user_cr"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # CREATE
    @classmethod
    # we store the data in a dictionary coming from request.form in template
    # we passing data through so we add data with cls
    def create_user(cls, data):
        query = """
                INSERT INTO users (first_name, last_name, email)
                VALUES ( %(first_name)s, %(last_name)s, %(email)s)
                """
        return connectToMySQL(cls.DB).query_db(query,data)

    # READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []

        for user in results:
            #make object and add to list
            users.append( cls(user) )
        #this is important to return *it goes flush with for loop*
        return users

    @classmethod
    def get_one(cls, id):
        query = """SELECT * FROM users
                WHERE id = %(id)s; """
        results = connectToMySQL(cls.DB).query_db(query, {"id": id})
        #results would be in a list 
        return cls(results[0])

    # UPDATE
    @classmethod
    def update(cls, data):
        query = """UPDATE users
                SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
                WHERE id = %(id)s; """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    # DELETE
    @classmethod
    def delete(cls, id):
        query = """DELETE FROM users 
                WHERE id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query, {'id': id})
        return results