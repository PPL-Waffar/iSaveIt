from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from importlib import import_module
from django.conf import settings
from .models import Payment
from user.models import *
import json
from django.http.response import HttpResponse, HttpResponseForbidden, JsonResponse
# Create your views here.
from django.views.decorators.http import require_http_methods
@require_http_methods(["POST"])
@csrf_exempt
def flutter_add_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        session_id = data.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        pay_name = data.get('input_payname')
        pay_amount = data.get('input_payamount')
        pay_date = data.get('input_paydate')
        pay_categories = data.get('input_paycategories')
        payment_choice = data.get('input_paymentchoice')
        owninguser = Account.objects.get(email = email)
        new_payment = Payment(user_payment = owninguser,pay_name = pay_name, pay_date = pay_date, pay_amount= pay_amount, pay_categories=pay_categories, payment_choice =payment_choice)
        new_payment.save()
    return JsonResponse({'isSuccessful':True},safe = False)

@require_http_methods(["GET"])
@csrf_exempt
def flutter_get_payment(request):
    if request.method == 'GET':
        session_id = request.GET.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        owninguser = Account.objects.get(email = email)
        payments = Payment.objects.filter(user_payment = owninguser)
        payment_list = []
        for payment in payments:
            payment_list.append({
                'pay_name': payment.pay_name,
                'pay_amount': payment.pay_amount,
                'pay_date': payment.pay_date,
                'pay_categories': payment.pay_categories,
                'payment_choice': payment.payment_choice,
            })
        return JsonResponse(payment_list,safe = False)
<<<<<<< HEAD
=======
    return HttpResponseForbidden()

>>>>>>> b236df0 ([RED] Added user connection to view payment)

@csrf_exempt
@require_http_methods(["POST"])
def flutter_update_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        session_id = data.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        pay_name = data.get('input_payname')
        new_pay_amount = data.get('input_payamount')
        new_pay_date = data.get('input_paydate')
        new_pay_categories = data.get('input_paycategories')
        new_payment_choice = data.get('input_paymentchoice')
        owninguser = Account.objects.get(email = email)
        payment = Payment.objects.get(user_payment = owninguser, pay_name = pay_name)
        payment.pay_amount = new_pay_amount
        payment.pay_date = new_pay_date
        payment.pay_categories = new_pay_categories
        payment.payment_choice = new_payment_choice
        payment.save()
        return JsonResponse({'isSuccessful':True},safe = False)

@csrf_exempt
@require_http_methods(["DELETE"])
def flutter_delete_payment(request):
    if request.method == 'DELETE':
        data = json.loads(request.body.decode("utf-8"))
        session_id = data.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        pay_name = data.get('input_payname')
        owninguser = Account.objects.get(email = email)
        payment = Payment.objects.get(user_payment = owninguser, pay_name = pay_name)
        payment.delete()
        return JsonResponse({'isSuccessful':True},safe = False)