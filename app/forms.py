from flask_wtf import FlaskForm
from wtforms.fields import (BooleanField, DateField,
                            StringField, SubmitField, TextAreaField, TimeField)
from wtforms.validators import InputRequired
from wtforms.widgets.html5 import DateInput, TimeInput


class AppointmentForm(FlaskForm):
    name = StringField(label='Name', validators=[InputRequired()])
    start_date = DateField('Start date', validators=[
                           InputRequired()], widget=DateInput())
    start_time = TimeField('Start time', validators=[
                           InputRequired()], widget=TimeInput())
    end_date = DateField('End date', validators=[
                         InputRequired()], widget=DateInput())
    end_time = TimeField('End time', validators=[
                         InputRequired()], widget=TimeInput())
    description = TextAreaField('Description', validators=[InputRequired()])
    private = BooleanField('Private?')
    submit = SubmitField('Create an Appointment')
