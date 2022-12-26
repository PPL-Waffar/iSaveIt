from importlib import import_module
import json

from expense.models import Expense
from payment.models import Payment
from transaction.models import Transaction
from .models import *
from user.models import Account
from .models import Pocket
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings

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
        new_pocket = Pocket(user_pocket = owninguser ,pocket_name = pocket_name, pocket_budget = pocket_budget,pocket_default = pocket_budget)
        new_pocket.save()
    return JsonResponse({'isSuccessful':True},safe = False)

@csrf_exempt
def get_pocket(request):
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
            'pocket_budget' : formatrupiah(pocket.pocket_budget),
            'pocket_balance' : formatrupiah(pocket.pocket_default)
        })
    data = json.dumps(pocket_list)
    return HttpResponse(data, content_type='application/json')

@require_http_methods(["DELETE"])
@csrf_exempt
def delete_pocket(request):
    if request.method == "DELETE":
        data = json.loads(request.body.decode('utf-8'))
        session_id = data.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        pocket = request.GET.get('id')
        email = session.get('_auth_user_id')
        pocket_name = data.get('input_pocketname')
        owninguser = Account.objects.get(email = email)
        pocket = Pocket.objects.get(user_pocket = owninguser, pocket_name = pocket_name)
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
        pocketlama = data.get('pocketold')
        new_pocket_name = data.get('input_pocketname')
        new_pocket_budget = data.get('input_pocketbudget')
        owninguser = Account.objects.get(email = email)
        pocket = Pocket.objects.get(user_pocket = owninguser, pocket_name = pocketlama)
        pocket.pocket_budget = new_pocket_budget
        pocket.save()
    return JsonResponse({'isSuccessful':True},safe = False)

@csrf_exempt
def all_balance(request):
    session_id = request.GET.get('session_id')
    engine = import_module(settings.SESSION_ENGINE)
    sessionstore = engine.SessionStore
    session = sessionstore(session_id)
    email = session.get('_auth_user_id')
    owninguser = Account.objects.get(email = email)
    pockets = Pocket.objects.filter(user_pocket = owninguser)
    total = 0
    totalbalance = []
    for pocket in pockets:
        total += pocket.pocket_budget
    totalbalance.append(formatrupiah(total))
    data = json.dumps((totalbalance))
    return HttpResponse(data,content_type='application/json')

@csrf_exempt   
def all_expense(request):
    session_id = request.GET.get('session_id')
    engine = import_module(settings.SESSION_ENGINE)
    sessionstore = engine.SessionStore
    session = sessionstore(session_id)
    email = session.get('_auth_user_id')
    pocket = request.GET.get('input_pocketname')
    owninguser = Account.objects.get(email = email)
    allexpense = Expense.objects.filter(user_expense = owninguser,expense_pocket = pocket)
    total = 0
    for expense in allexpense:
        total += expense.expense_amount
    alltransaction = Transaction.objects.filter(user_transaction = owninguser,transaction_pocket = pocket)
    for transaction in alltransaction:
        total += transaction.transaction_amount
    allpayment = Payment.objects.filter(user_payment = owninguser,pay_categories = pocket)
    for payment in allpayment:
        total += payment.pay_amount
    totallist = []
    totallist.append(formatrupiah(total))
    data = json.dumps(totallist)
    return HttpResponse(data,content_type='application/json')
