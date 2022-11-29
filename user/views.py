from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,logout,login
import json
from importlib import import_module
from django.conf import settings
from .models import *
import json
from django.http.response import HttpResponse, HttpResponseForbidden, JsonResponse
from django.contrib.auth import login
# Create your views here.
@csrf_exempt
def flutter_register_user(request):
    if request.method == "POST":
        raw = request.body.decode('utf-8')
        cleaned = json.loads(raw)
        register_user = Account.objects.create(role_users=True, email=cleaned["email"], name = cleaned["name"])
        register_user.set_password(cleaned["password"])
        try:
            register_user.save()
        except:
            return HttpResponse(status=409)
        login(request, register_user)
        return JsonResponse({"session-id": request.session.session_key,"is_staff": False, "role_users": True, "email": register_user.email, "name": register_user.name})

@csrf_exempt
def flutter_user_login(request):
    if request.method == "POST":
        data = request.body.decode("utf-8")
        cleaned_data = json.loads(data)
        email = cleaned_data["email"]
        password = cleaned_data["password"]
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return JsonResponse({"session-id": request.session.session_key, "is_staff": False, "role_users": True, "email": user.email})

@csrf_exempt
def flutter_get_user_info(request):
    session_id = request.GET.get('session_id')
    engine = import_module(settings.SESSION_ENGINE)
    sessionstore = engine.SessionStore
    session = sessionstore(session_id)
    email = session.get('_auth_user_id')
    user = Account.objects.get(email=email)
    response_data = {
        "session-id": request.session.session_key,
        "is_staff": False,
        "role_users": True,
        "email": user.email,
        "name": user.name
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def flutter_edit_user(request):
    if request.method == "POST":
        data = request.body.decode("utf-8")
        cleaned_data = json.loads(data)
        session_id = cleaned_data.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        user = Account.objects.get(email=email)
        user.name = cleaned_data.get('name')
        user.save()
        return JsonResponse({"session-id": request.session.session_key, "is_staff": False, "role_users": True, "email": user.email, "name": user.name})
    