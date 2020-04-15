from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class Starter(FlaskForm):
    starter = StringField('Starter', validators=[DataRequired(), Length(min=2, max=20)])