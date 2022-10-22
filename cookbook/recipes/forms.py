from django import forms

class PortionsForm(forms.Form):
    your_portions = forms.IntegerField(label='', max_value=999)

    def __init__(self, *args, **kwargs):
        self.portions = kwargs.pop('default_portions')
        super(PortionsForm, self).__init__(*args, **kwargs)
        self.fields['your_portions'].initial = self.portions

    def process(self, request):
        request.session['portions'] = self.cleaned_data['your_portions']