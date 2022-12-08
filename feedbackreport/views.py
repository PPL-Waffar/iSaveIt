from importlib import import_module
import json
from user.models import Account
from feedbackreport.models import Feedback
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
import datetime
import dateutil.parser


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
        feedback_rating = data.get('input_feedback_rating')
        feedback_goal = data.get('input_feedback_goal')
        feedback_text = data.get('input_feedback_text')
        feedback_text2 = data.get('input_feedback_text2')
        feedback_comment = data.get('input_feedback_comment')
        feedback_date = data.get('input_feedback_date')
        user_feedback = Account.objects.get(email=email)
        feedback = Feedback(user_feedback=user_feedback, feedback_rating=feedback_rating, feedback_goal=feedback_goal, feedback_text=feedback_text, feedback_text2=feedback_text2, feedback_comment=feedback_comment, feedback_date=feedback_date)
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
        feedback_id = data.get('id')
        owninguser = Account.objects.get(email = email)
        feedback_report = Feedback.objects.get(user_feedback = owninguser, id = feedback_id)
        feedback_report.delete()
    return JsonResponse({'isSuccessful':True},safe = False)

@require_http_methods(["GET"])
@csrf_exempt
def view_feedback_report(request):
    if request.method == "GET":
        session_id = request.GET.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        owninguser = Account.objects.get(email = email)
        feedback_report = Feedback.objects.filter(user_feedback = owninguser)
        feedback_report_list = []

        for feedback in feedback_report:
            time = dateutil.parser.parse(str(feedback.feedback_date))
            time_between_insertion = datetime.datetime.today() - time
            if  time_between_insertion.days>90:
                feedback_check = "More than 90 days"

            else:
                feedback_check = "Below 90 days"
            feedback_report_list.append({
                'feedback_rating': feedback.feedback_rating,
                'feedback_goal': feedback.feedback_goal,
                'feedback_text': feedback.feedback_text,
                'feedback_text2': feedback.feedback_text2,
                'feedback_comment': feedback.feedback_comment,
                'feedback_date': feedback.feedback_date,
                'feedback_check': feedback_check
            })
        return JsonResponse(feedback_report_list,safe = False)