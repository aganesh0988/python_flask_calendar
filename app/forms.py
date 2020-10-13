from flask_wtf import FlaskForm
from wtforms.fields import (BooleanField, DateField,
                            StringField, SubmitField, TextAreaField, TimeField)
from wtforms.validators import InputRequired, ValidationError
from wtforms.widgets.html5 import DateInput, TimeInput
from datetime import datetime


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

    def validate_end_date(form, field):
        end = datetime.combine(form.end_date.data, form.end_time.data)
        start = datetime.combine(form.start_date.data, form.start_time.data)
        if start >= end:
            msg = "End data/time must come after start date/time"
            raise ValidationError(msg)
