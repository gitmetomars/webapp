from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.widgets import Input
from wtforms.validators import Required, Email
from wtforms import ValidationError

import phonenumbers


class TelephoneForm(FlaskForm):
    country_code = IntegerField('Country Code', validators=[Required()])
    area_code    = IntegerField('Area Code/Exchange', validators=[Required()])
    number       = TextField('Number')

class ContactForm(FlaskForm):
    name = TextField(u'Your name', validators=[Required()])
    email = TextField(u'Your email address', validators=[Email()])
    phone = FormField(TelephoneForm)
    message = TextAreaField('Your message:', [Required()])

    submit = SubmitField(u'Signup')


