from django import forms


class PortionsForm(forms.Form):
    your_portions = forms.IntegerField(label='', max_value=999)

    def __init__(self, *args, **kwargs):
        self.portions = kwargs.pop('default_portions')
        super().__init__(*args, **kwargs)
        self.fields['your_portions'].initial = self.portions

    def process(self, request):
        request.session['portions'] = self.cleaned_data['your_portions']

        if "btn_down" in request.POST:
            request.session['portions'] -= 1
        if "btn_up" in request.POST:
            request.session['portions'] += 1
        if request.session['portions'] < 1:
            request.session['portions'] = 1
        if request.session['portions'] > 999:
            request.session['portions'] = 999
