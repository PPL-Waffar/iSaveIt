from django.shortcuts import render
from newsletter.forms import NewsletterForm
from newsletter.models import Newsletter
import json
from django.http import HttpResponse, JsonResponse

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

