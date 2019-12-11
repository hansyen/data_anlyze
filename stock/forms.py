from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class StockForm(FlaskForm):
    start_year = StringField('Start Year: (ex:2019)', validators=[DataRequired()])
    start_month = StringField('Start Month: (ex:1)', validators=[DataRequired()])
    start_date = StringField('Start Date: (ex:1)', validators=[DataRequired()])
    end_year = StringField('End Year: (ex:2019)', validators=[DataRequired()])
    end_month = StringField('End Month: (ex:2)', validators=[DataRequired()])
    end_date = StringField('End Date: (ex:1)', validators=[DataRequired()])
    search_stock = StringField('Search For: (ex:2330.TW, AAPL, GOOG)', validators=[DataRequired()])
    submit = SubmitField('Go')

class StockSelectForm(FlaskForm):
    choices = [('high', 'High'),
               ('low', 'Low'),
               ('open', 'Open'),
               ('close', 'Close'),
               ('volume', 'Volume'),
               ('adj_close', 'Adj Close')]
    select = SelectField('Choose one : ', choices=choices)
    submit = SubmitField('Plot')
