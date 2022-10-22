from .forms import PortionsForm

def inject_form(request):
    if 'portions' not in request.session:
        portions = 4
    else:
        portions = request.session['portions']

    return {'form': PortionsForm(default_portions=portions)}