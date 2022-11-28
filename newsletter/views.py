import json
from django.shortcuts import render
from newsletter.forms import NewsletterForm
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from newsletter.models import Newsletter

@require_http_methods(["GET", "POST"])
def add_newsletter(request):
    context = {}
    context['form'] = NewsletterForm(request.POST, request.FILES)
    if context['form'].is_valid():
        context['form'].save()
        context['form'] = NewsletterForm()
    return render(request, 'newsletter.html', context)


@require_http_methods(["GET"])
@csrf_exempt
def view_detail_newsletter(request, id):
    if request.method == "GET":
        newsletter_id = id
        newsletter = Newsletter.objects.get(id=newsletter_id)
        newsletter_list = []
        newsletter_list.append({
            'newsletter_category': newsletter.newsletter_category,
            'newsletter_text': newsletter.newsletter_text,
            'newsletter_picture': json.dumps(str(newsletter.newsletter_picture.url)),
        })
        return JsonResponse({'isSuccessful':True, 'newsletter': newsletter_list},safe = False)