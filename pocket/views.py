from importlib import import_module
import json

from user.models import Account
from .models import Pocket
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings

@require_http_methods(["POST"])
@csrf_exempt
def add_pocket(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        session_id = data.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        pocket_name = data.get('input_pocketname')
        pocket_budget = data.get('input_pocketbudget')
        owninguser = Account.objects.get(email = email)
        new_pocket = Pocket(user_pocket = owninguser ,pocket_name = pocket_name, pocket_budget = pocket_budget)
        new_pocket.save()
    return JsonResponse({'isSuccessful':True},safe = False)

@require_http_methods(["GET"])
def get_pocket(request):
    if request.method == "GET":
        session_id = request.GET.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        owninguser = Account.objects.get(email = email)
        pockets = Pocket.objects.filter(user_pocket = owninguser)
        pocket_list = []
        for pocket in pockets:
            pocket_list.append({
                'pocket_name' : pocket.pocket_name,
                'pocket_budget' : pocket.pocket_budget
            })
        return JsonResponse(pocket_list,safe = False)

@require_http_methods(["DELETE"])
@csrf_exempt
def delete_pocket(request):
    if request.method == "DELETE":
        data = json.loads(request.body.decode('utf-8'))
        session_id = data.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        owninguser = Account.objects.get(email = email)
        pocket = Pocket.objects.filter(user_pocket = owninguser)
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
        pocket_name = data.get('input_pocketname')
        pocket_budget = data.get('input_pocketbudget')
        pocket = Pocket.objects.filter(user_pocket = owninguser)
        pocket.pocket_name = pocket_name
        pocket.pocket_budget = pocket_budget
        pocket.save()
    return JsonResponse({'isSuccessful':True},safe = False)

# @require_http_methods(["DELETE"])
# @csrf_exempt
# def delete_pocket(request):
#     if request.method == "DELETE":
#         data = json.loads(request.body.decode('utf-8'))
#         session_id = data.get('session_id')
#         engine = import_module(settings.SESSION_ENGINE)
#         sessionstore = engine.SessionStore
#         session = sessionstore(session_id)
#         email = session.get('_auth_user_id')
#         owninguser = Account.objects.get(email = email)
#         pocket = Pocket.objects.get(user_pocket = owninguser)
#         pocket.delete()
#     return JsonResponse({'isSuccessful':True},safe = False)


# @require_http_methods(["POST"])
# @csrf_exempt
# def edit_pocket(request):
#     if request.method == "POST":
#         data = json.loads(request.body.decode('utf-8'))
#         session_id = data.get('session_id')
#         engine = import_module(settings.SESSION_ENGINE)
#         sessionstore = engine.SessionStore
#         session = sessionstore(session_id)
#         email = session.get('_auth_user_id')
#         owninguser = Account.objects.get(email = email)
#         pocket_name = data.get('input_pocketname')
#         pocket_budget = data.get('input_pocketbudget')
#         pocket = Pocket.objects.get(user_pocket = owninguser)
#         pocket.pocket_name = pocket_name
#         pocket.pocket_budget = pocket_budget
#         pocket.save()
#     return JsonResponse({'isSuccessful':True},safe = False)