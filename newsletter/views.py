from django.shortcuts import render

from newsletter.models import Newsletter

def index(request):
    return render(request, 'newsletter.html')

def add_newsletter(request):
    if request.method == 'POST':
        newsletter_text = request.POST['newsletter_text']
        newsletter_picture = request.POST['newsletter_picture']
        newsletter_category = request.POST['newsletter_category']
        newsletter = Newsletter(newsletter_text=newsletter_text, newsletter_picture=newsletter_picture, newsletter_category=newsletter_category)
        newsletter.save()
    return render(request, 'newsletter.html')