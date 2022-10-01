import json
from .models import Pocket
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from importlib import import_module
from django.conf import settings
from user.models import Account

@require_http_methods(["POST"])
@csrf_exempt
def add_pocket(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        pocket_name = data['pocket_name']
        pocket_budget = data['pocket_budget']
        new_pocket = Pocket(pocket_name=pocket_name, pocket_budget=pocket_budget)
        new_pocket.save()
    return JsonResponse({'isSuccessful':True},safe = False)


@require_http_methods(["POST"])
@csrf_exempt
def delete_pocket(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        session_id = data.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        owninguser = Account.objects.get(email = email)
        pocket = Pocket.objects.get(user_pocket = owninguser)
        pocket.delete()
    return JsonResponse({'isSuccessful':True},safe = False)


@require_http_methods(["POST"])
@csrf_exempt
def edit_pocket(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        session_id = data.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        owninguser = Account.objects.get(email = email)
        name = data.get('name')
        budget = data.get('budget')
        pocket = Pocket.objects.get(user_pocket = owninguser)
        pocket.name = name
        pocket.budget = budget
        pocket.save()
    return JsonResponse({'isSuccessful':True},safe = False)

