from django.shortcuts import render
from Properties.models import Properties


# Create your views here.
def catalog(request):
    context = {'properties': Properties.objects.all()}
    return render(request, 'Properties/Catalog.html', context)
