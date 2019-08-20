from flask_wtf import Form
from wtforms.fields import DecimalField, StringField, RadioField, SubmitField
from wtforms.validators import DataRequired


class Message(Form):
    original_text = StringField('Text to cipher/uncipher', validators=[DataRequired(message="only alpha values")])
    key = DecimalField('Key')
    rAction = RadioField('Action', choices=[('e', 'Encrypt'), ('d', 'Decrypt'), ('b', 'Brute')])
    submit = SubmitField('Execute')


