from importlib import import_module
import json
from user.models import Account
from feedbackreport.models import Feedback
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings

@require_http_methods(["POST"])
@csrf_exempt
def add_feedback_report(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        session_id = data.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        feedback_title = data.get('input_feedback_title')
        feedback_feature = data.get('input_feedback_feature')
        feedback_textbox = data.get('input_feedback_texbox')
        owninguser = Account.objects.get(email = email)
        new_feedback_report = Feedback(user_feedback = owninguser, feedback_title = feedback_title, feedback_feature = feedback_feature, feedback_textbox = feedback_textbox)
        new_feedback_report.save()
    return JsonResponse({'isSuccessful':True},safe = False)

@require_http_methods(["DELETE"])
@csrf_exempt
def delete_feedback_report(request):
    if request.method == "DELETE":
        data = json.loads(request.body.decode("utf-8"))
        session_id = data.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        feedback_title = data.get('input_feedback_title')
        owninguser = Account.objects.get(email = email)
        feedback_report = Feedback.objects.get(user_pocket = owninguser, feedback_title = feedback_title)
        feedback_report.delete()
    return JsonResponse({'isSuccessful':True},safe = False)