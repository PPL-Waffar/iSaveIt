from django.shortcuts import render
from newsletter.forms import NewsletterForm
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
def add_newsletter(request):
    if request.method == 'POST':
        context = {}
        context['form'] = NewsletterForm(request.POST, request.FILES)
        if context['form'].is_valid():
            context['form'].save()
            context['form'] = NewsletterForm()
            return render(request, 'newsletter.html', context)