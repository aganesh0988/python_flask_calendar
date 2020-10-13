from flask import Blueprint, render_template
import os
import psycopg2

bp = Blueprint('main', __name__, '')

CONNECTION_PARAMETERS = {
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASS'),
    'dbname': os.environ.get('DB_NAME'),
    'host': os.environ.get('DB_HOST')
}


@bp.route('/')
def main():
    # create connection object as conn to connect to db
    with psycopg2.connect(CONNECTION_PARAMETERS) as conn:
        # create cursor object as curs to interact with db
        with conn.cursor() as curs:
            # execute sql command to alter db, retrieve data, etc.
            # curs.execute(<sql command>)

            # add data extracted from db to render_template arg list
            # this displays db info in specified HTML template
    return render_template('main.html')
