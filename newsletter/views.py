import json
from django.shortcuts import render
from newsletter.forms import NewsletterForm
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from newsletter.models import Newsletter
from django.http import HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404, render,HttpResponseRedirect

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

