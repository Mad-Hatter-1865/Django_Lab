from django.forms import ModelForm
from .models import Expansion

class ExpansionForm(ModelForm):
    class Meta:
        model = Expansion
        fields = ['extitle', 'rely']
