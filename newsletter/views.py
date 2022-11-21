from django.shortcuts import render
from newsletter.forms import NewsletterForm
from newsletter.models import Newsletter

def add_newsletter(request):
    if request.method == 'POST':
        context = {}
        context['form'] = NewsletterForm(request.POST, request.FILES)
        if context['form'].is_valid():
            context['form'].save()
            context['form'] = NewsletterForm()
            return render(request, 'newsletter.html', context)