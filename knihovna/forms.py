from django import forms
from .models import Kniha


class KnihaForm(forms.ModelForm):
    class Meta:
        model = Kniha
        fields = '__all__'
        widgets = {
            'autori': forms.CheckboxSelectMultiple(),
            'zanry': forms.CheckboxSelectMultiple(),
        }