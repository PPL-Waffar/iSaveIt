from urllib import response
from django.shortcuts import render

from pocket.forms import PocketForm
from .models import Pocket
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect

@csrf_exempt
def index(request): 
    
    if request.method == "POST":
        
        form = PocketForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("")
    
    pocket = Pocket.objects.all()
    response = {'pocket': pocket}


    return render(request, 'pocket.html', {'pocket': pocket})
