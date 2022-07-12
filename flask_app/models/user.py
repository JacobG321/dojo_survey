from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Users:
    db_name = 'dojo_survey_schema'
    def __init__( self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.dojo_location = data['dojo_location']
        self.favorite_language = data['favorite_language']
        self.comments = data['comments']


    @classmethod
    def save( cls, data ):
        query = "INSERT INTO user ( first_name, last_name, dojo_location, favorite_language, comments ) VALUES ( %(first_name)s, %(last_name)s, %(dojo_location)s, %(favorite_language)s, %(comments)s)"
        return connectToMySQL( cls.db_name ).query_db( query, data )


    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['first_name']) < 3:
            flash('First name must be more than 3 characters')
            is_valid = False
        if len(data['last_name']) < 3:
            flash('Last name must be more than 3 characters')
            is_valid = False
        if len(data['comments']) > 255:
            flash('Comments must be less than 255 characters')
            is_valid = False
        return is_valid