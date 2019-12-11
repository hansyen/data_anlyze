from flask_wtf import FlaskForm
from wtforms import SelectField, StringField


class BillingTicketSearchForm(FlaskForm):
    choices = [('td', 'Ticket Number'),
               ('name', 'User Name'),
               ('card_type', 'Card Type'),
               ('errcode', 'Error Number'),
               ('status', 'Status')]
    select = SelectField('Search for Billing Ticket:', choices=choices)
    search = StringField('')

