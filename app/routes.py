from flask import Blueprint, render_template, redirect
import os
import psycopg2
from .forms import AppointmentForm
from datetime import datetime


bp = Blueprint('main', __name__, '')

CONNECTION_PARAMETERS = {
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASS'),
    'dbname': os.environ.get('DB_NAME'),
    'host': os.environ.get('DB_HOST')
}

# add methods=['GET', 'POST'] so this route can accept form submission


@bp.route('/', methods=['GET', 'POST'])
def main():
    d = datetime.now()
    return redirect(url_for('.daily', year=d.year, month=d.month, day=d.day))

    # form = AppointmentForm()
    # if form.validate_on_submit():
    #     # do stuff - send data to db?
    #     params = {
    #         'name': form.name.data,
    #         'start_datetime': datetime.combine(form.start_date.data, form.start_time.data),
    #         'end_datetime': datetime.combine(form.end_date.data, form.end_time.data),
    #         'description': form.description.data,
    #         'private': form.private.data
    #     }
    #     # create connection object as conn to connect to db
    #     with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    #         # create cursor object as curs to interact with db
    #         with conn.cursor() as curs:
    #             # execute sql command to alter db, retrieve data, etc.
    #             # curs.execute("<sql insert statement>")
    #             placeholders = ', '.join(['%s'] * len(params))
    #             columns = ', '.join(params.keys())
    #             sql = "INSERT INTO appointments ( %s ) VALUES ( %s )" % (
    #                 columns, placeholders)
    #             curs.execute(sql, list(params.values()))
    #             return redirect('/')
    # # create connection object as conn to connect to db
    # with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    #     # create cursor object as curs to interact with db
    #     with conn.cursor() as curs:
    #         # execute sql command to alter db, retrieve data, etc.
    #         # curs.execute("<sql command>")
    #         curs.execute(
    #             "SELECT id, name, start_datetime, end_datetime FROM appointments ORDER BY start_datetime;")
    #         rows = curs.fetchall()
    #         print(rows)
    #         # add data extracted from db to render_template arg list
    #         # this displays db info in specified HTML template
    # return render_template('main.html', rows=rows, form=form)


@bp.route('/<int:year>/<int:month>/<int:day>', methods=['GET', 'POST'])
def daily(year, month, day):
    # today = datetime.combine(year, month, day)
    form = AppointmentForm()
    if form.validate_on_submit():
        # do stuff - send data to db?
        params = {
            'name': form.name.data,
            'start_datetime': datetime.combine(form.start_date.data, form.start_time.data),
            'end_datetime': datetime.combine(form.end_date.data, form.end_time.data),
            'description': form.description.data,
            'private': form.private.data
        }
        # column_names = list(params.keys())
        # column_values = list(params.values())
        # create connection object as conn to connect to db
        with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
            # create cursor object as curs to interact with db
            with conn.cursor() as curs:
                # execute sql command to alter db, retrieve data, etc.
                # curs.execute("<sql insert statement>")
                placeholders = ', '.join(['%s'] * len(params))
                columns = ', '.join(params.keys())
                sql = "INSERT INTO appointments ( %s ) VALUES ( %s )" % (
                    columns, placeholders)
                curs.execute(sql, list(params.values()))
                return redirect('/')
    # create connection object as conn to connect to db
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        # create cursor object as curs to interact with db
        with conn.cursor() as curs:
            # execute sql command to alter db, retrieve data, etc.
            # curs.execute("<sql command>")
            curs.execute(f"""
                SELECT id, name, start_datetime, end_datetime
                FROM appointments
                ORDER BY start_datetime;
                """)
            rows = curs.fetchall()
            print(rows)
            # add data extracted from db to render_template arg list
            # this displays db info in specified HTML template
    return render_template('main.html', rows=rows, form=form)
