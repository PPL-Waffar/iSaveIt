import json
from django.shortcuts import render
from newsletter.forms import NewsletterForm
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from newsletter.models import Newsletter
from django.http import HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404, render,HttpResponseRedirect

from newsletter.models import Newsletter

def add_newsletter(request):
    if require_http_methods(["POST"]):
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
        