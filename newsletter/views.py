from django.shortcuts import render
from newsletter.forms import NewsletterForm
from newsletter.models import Newsletter
import json
from django.http import HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404, render,HttpResponseRedirect

def index(request):
    return render(request, 'newsletter.html')

def add_newsletter(request):
    if request.method == 'POST':
        context = {}
        context['form'] = NewsletterForm(request.POST, request.FILES)
        if context['form'].is_valid():
            context['form'].save()
            context['form'] = NewsletterForm()
            return render(request, 'newsletter.html', context)
    else:
        context = {}
        context['form'] = NewsletterForm()
        return render(request, 'newsletter.html', context)

def view_newsletter_list(request):
    all_newsletter = Newsletter.objects.all()
    newsletter_list = []
    for newsletter in all_newsletter:
        newsletter_list.append({
            'newsletter_text' : newsletter.newsletter_text,
            'newsletter_picture' : newsletter.newsletter_picture,
            'newsletter_category' : newsletter.newsletter_category,
        })
    data = json.dumps(newsletter_list)
    return HttpResponse(data, content_type='application/json')

def delete_newsletter(request,id):
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Newsletter, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("list/")
    
    return render(request, "delete_view.html", context)

def newsletterhtmk(request):
    obj=Newsletter.objects.all()
    return render(request,'list.html',{"obj":obj})

def update_newsletter(request,id):
    if request.method == 'POST':
        obj = get_object_or_404(Newsletter, id = id)
        form = NewsletterForm(request.POST, request.FILES, instance = obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("list/")
    else:
        obj = get_object_or_404(Newsletter, id = id)
        form = NewsletterForm(instance = obj)
        return render(request, 'edit_newsletter.html', {'form':form})


