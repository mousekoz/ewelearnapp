from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

	# TODO: forgot password link

# RegistrationForm
	# username, email, password field, retype password field, submit
# ChallengeForm
	# answer, submit
# EditProfileForm
	# username, email, password field, retype password field, submit