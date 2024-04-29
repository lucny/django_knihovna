from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button
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


class BookForm(forms.ModelForm):
    class Meta:
        model = Kniha
        fields = ['titul', 'obsah', 'pocet_stran',
                  'rok_vydani', 'autori', 'obalka',
                  'vydavatelstvi', 'zanry']
        widgets = {
            'titul': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Zadej titul knihy'}),
            'obsah': forms.Textarea(attrs={'class': 'form-control',
                                           'placeholder': 'Zadej obsah knihy'}),
            'pocet_stran': forms.NumberInput(attrs={'class': 'form-control',
                                           'value': '200', 'min': 10, 'max': 2000}),
            'autori': forms.SelectMultiple(attrs={'class': 'form-control',
                                           'placeholder': 'Zadej jednoho nebo více autorů'}),
            'zanry': forms.SelectMultiple(attrs={'class': 'form-control',
                                           'placeholder': 'Zadej jeden nebo více žánrů'}),
            'vydavatelstvi': forms.Select(attrs={'class': 'form-control',
                                           'placeholder': 'Zadej jedno vydavatelství'}),
            'rok_vydani': forms.NumberInput(attrs={'class': 'form-control',
                                           'value': '2023', 'min': 1000, 'max': 2023}),
            'obalka': forms.ClearableFileInput(attrs={'class': 'form-control',
                                           'placeholder': 'Vlož obrázek'}),
        }
        labels = {
            'titul': 'Titul knihy',
            'obsah': 'Stručný obsah knihy',
            'pocet_stran': 'Počet stran',
            'autori': 'Autoři knih',
            'zanry': 'Žánry',
            'vydavatelstvi': 'Vydavatelství',
            'rok_vydani': 'Vydání',
            'obalka': 'Obálka',
        }
        required = {
            'title': True,
            'obsah': False,
            'pocet_stran': False,
            'autori': True,
            'zanry': False,
            'vydavatelstvi': False,
            'vydani': False,
            'obalka': False,
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Fieldset(
                'Informace o knize',
                'titul',
                'obsah',
                'pocet_stran',
                'autori',
                'zanry',
                'vydavatelstvi',
                'rok_vydani',
                'obalka',
            ),
            FormActions(
                ButtonHolder(
                    Submit('submit', 'Uložit', css_class='btn-primary mr-2'),
                    Button('cancel', 'Storno', css_class='btn-secondary',
                           onclick='window.history.back();'),
                    css_class='d-flex'
                )
            ),
        )
