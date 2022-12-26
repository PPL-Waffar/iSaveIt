from importlib import import_module
import json
from user.models import Account
from feedbackreport.models import Feedback
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
import datetime



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
        feedback_rating = data.get('feedback1')
        feedback_goal = data.get('feedback2')
        feedback_text = data.get('feedback3')
        feedback_text2 = data.get('feedback4')
        feedback_comment = data.get('feedback5')
        user_feedback = Account.objects.get(email=email)
        feedback = Feedback(user_feedback=user_feedback, feedback_rating=feedback_rating, feedback_goal=feedback_goal, feedback_text=feedback_text, feedback_text2=feedback_text2, feedback_comment=feedback_comment)
        feedback.save()
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
        feedback_id = request.GET.get('input_id')
        owninguser = Account.objects.get(email = email)
        feedback_report = Feedback.objects.get(user_feedback = owninguser, customer_ID = feedback_id)
        feedback_report.delete()
    return JsonResponse({'isSuccessful':True},safe = False)


@csrf_exempt
def view_feedback_report(request):
    session_id = request.GET.get('session_id')
    engine = import_module(settings.SESSION_ENGINE)
    sessionstore = engine.SessionStore
    session = sessionstore(session_id)
    email = session.get('_auth_user_id')
    owninguser = Account.objects.get(email = email)
    feedback_report = Feedback.objects.filter(user_feedback = owninguser)
    feedback_report_list = []
    for feedback in feedback_report:
        feedback_report_list.append({
            'feedback_id' : feedback.customer_ID,
            'feedback_rating': feedback.feedback_rating,
            'feedback_goal': feedback.feedback_goal,
            'feedback_text': feedback.feedback_text,
            'feedback_text2': feedback.feedback_text2,
            'feedback_comment': feedback.feedback_comment,
            'feedback_date': str(feedback.date)[0:10]
        })
    data = json.dumps(feedback_report_list)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def view_feedback_detail(request):
    session_id = request.GET.get('session_id')
    engine = import_module(settings.SESSION_ENGINE)
    sessionstore = engine.SessionStore
    session = sessionstore(session_id)
    email = session.get('_auth_user_id')
    feedback_id = request.GET.get('input_id')
    owninguser = Account.objects.get(email = email)
    feedback_report = Feedback.objects.get(user_feedback = owninguser, customer_ID = feedback_id)
    feedback_report_list = []
    feedback_report_list.append({
        'feedback_id' : feedback_report.customer_ID,
        'feedback_rating': feedback_report.feedback_rating,
        'feedback_goal': feedback_report.feedback_goal,
        'feedback_text': feedback_report.feedback_text,
        'feedback_text2': feedback_report.feedback_text2,
        'feedback_comment': feedback_report.feedback_comment,
        'feedback_date': str(feedback_report.date)[0:10]
    })
    data = json.dumps(feedback_report_list)
    return HttpResponse(data, content_type='application/json')
