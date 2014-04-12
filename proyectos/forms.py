from proyectos.models import Participante
from django import forms

class ParticipanteForm(forms.Form):
	email = forms.EmailField(help_text='* Recuerda usar el e-mail con el que te registraste.', label='e-mail')