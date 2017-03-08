from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	first_name = StringField('First name', validators = [DataRequired("Por favor, preencha com o seu primeiro nome.")])
	last_name = StringField('Last Name', validators = [DataRequired("Por favor, preencha com o seu ultimo nome.")])
	email = StringField('Email', validators = [DataRequired("Por favor, adicione um email."), Email("Pro favor, informe o seu email.")])
	password = PasswordField('Password', validators = [DataRequired("Por favor, adicione uma senha para sua conta."), Length(min=6, message="A senha deve ter 6 ou mais caracteres.")])
	submit = SubmitField('Sign up')

class LoginForm(Form):
	email = StringField('Email', validators = [DataRequired("Por favor, entre com seu email"), Email("Por favor, verife o seu email.")])
	password = PasswordField('Password', validators = [DataRequired("Por favor, adicione a sua senha.")])
	submit = SubmitField('Sign in')

class AddressForm(Form):
	address =  StringField('Address', validators=[DataRequired("Informe um endereco.")])
	submit = SubmitField("Search")