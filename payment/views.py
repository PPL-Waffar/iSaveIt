from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from importlib import import_module
from django.conf import settings
from .models import Payment
from user.models import *
from pocket.models import *
import json
from django.http.response import HttpResponse, HttpResponseForbidden, JsonResponse
# Create your views here.
from django.views.decorators.http import require_http_methods

def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3 :
        return 'Rp ' + y     
    else :
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p
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
        payment = Pocket.objects.get(pocket_name=pay_categories)
        payment_choice = data.get('input_paymentchoice')
        owninguser = Account.objects.get(email = email)
        new_payment = Payment(user_payment = owninguser,pay_name = pay_name, pay_date = pay_date, pay_amount= pay_amount, pay_categories=payment, payment_choice =payment_choice)
        new_payment.save()
    return JsonResponse({'isSuccessful':True},safe = False)

@csrf_exempt
def flutter_get_payment(request):
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
            'pay_amount': formatrupiah(payment.pay_amount),
            'pay_date': str(payment.pay_date)[:10],
            'pay_categories': str(payment.pay_categories.pocket_name),
            'payment_choice': payment.payment_choice,
        })
    data = json.dumps(payment_list)
    return HttpResponse(data, content_type='application/json')

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
        pay_name = request.GET.get('input_payment')
        owninguser = Account.objects.get(email = email)
        payment = Payment.objects.get(user_payment = owninguser, pay_name = pay_name)
        payment.delete()
        return JsonResponse({'isSuccessful':True},safe = False)

@csrf_exempt
def flutter_view_payment(request):
    session_id = request.GET.get('session_id')
    engine = import_module(settings.SESSION_ENGINE)
    sessionstore = engine.SessionStore
    session = sessionstore(session_id)  
    email = session.get('_auth_user_id')
    paymentname = request.GET.get('input_pocketname')
    owninguser = Account.objects.get(email = email)
    payments = Payment.objects.get(user_payment = owninguser, pay_name = paymentname)
    response_data = {
        'name': payments.pay_name,
        'amount' : formatrupiah(payments.pay_amount),
        'paydate': str(payments.pay_date)[0:10],
        'type': payments.payment_choice,
        'pocket':payments.pay_categories.pocket_name
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")

