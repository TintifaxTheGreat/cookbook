from django.http import HttpResponseRedirect

from .forms import PortionsForm

def change_portions(request):
    if request.method == 'POST':
        form = PortionsForm(request.POST, default_portions='')

        if form.is_valid():
            form.process(request)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        form = PortionsForm()

    context = {
        'form': form
    }
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
