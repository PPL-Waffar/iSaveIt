from importlib import import_module
import json

from user.models import Account
from .models import Pocket
from .models import Transaction
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
def input_transaction(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        session_id = data.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        transaction_payment_name = data.get('input_transaction_payment_name')
        transaction_amount = data.get('input_transaction_amount')
        transaction_date = data.get('input_transaction_date')
        transaction_transaction_type = data.get('input_transaction_transaction_type')
        transaction_payment_type = data.get('input_transaction_payment_type')
        transaction_pocket = data.get('input_transaction_pocket')
        owninguser = Account.objects.get(email = email)
        owning_pocket = Pocket.objects.get(pocket_name = transaction_pocket, user_pocket = owninguser)

        if transaction_payment_type == 'Expense':
            owning_pocket.pocket_budget -= int(transaction_amount)
            owning_pocket.save()
        else:
            owning_pocket.pocket_budget += int(transaction_amount)
            owning_pocket.save()
       
        new_transaction = Transaction(user_transaction = owninguser, transaction_payment_name = transaction_payment_name, 
                                        transaction_amount = transaction_amount, transaction_date = transaction_date, 
                                        transaction_transaction_type = transaction_transaction_type, 
                                        transaction_payment_type = transaction_payment_type, transaction_pocket = owning_pocket)
        new_transaction.save()
    return JsonResponse({'isSuccessful':True},safe = False)

@csrf_exempt
def get_transaction(request):
    session_id = request.GET.get('session_id')
    engine = import_module(settings.SESSION_ENGINE)
    sessionstore = engine.SessionStore
    session = sessionstore(session_id)
    email = session.get('_auth_user_id')
    try:
        owninguser = Account.objects.get(email = email)
        alltransaction = Transaction.objects.filter(user_transaction = owninguser)
        transaction_list = []
        for transaction in alltransaction:
            transaction_list.append({
                'transaction_payment_name' : transaction.transaction_payment_name,
                'transaction_amount' : transaction.transaction_amount,
                'transaction_date' : str(transaction.transaction_date),
                'transaction_transaction_type' : transaction.transaction_transaction_type,
                'transaction_payment_type' : transaction.transaction_payment_type,
                'transaction_pocket' : transaction.transaction_pocket.pocket_name
            })
        data = json.dumps(transaction_list)
        return HttpResponse(data, content_type='application/json')
    except Account.DoesNotExist or Transaction.DoesNotExist:
        return JsonResponse({'isSuccessful':False},status=404,safe = False)

@csrf_exempt
def delete_transaction(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            session_id = data.get('session_id')
            engine = import_module(settings.SESSION_ENGINE)
            sessionstore = engine.SessionStore
            session = sessionstore(session_id)
            email = session.get('_auth_user_id')
            owninguser = Account.objects.get(email = email)
            transaction_payment_name = data.get('transaction_payment_name')
            transaction = Transaction.objects.get(user_transaction = owninguser, transaction_payment_name = transaction_payment_name)
            transaction_pocket = data.get('input_transaction_pocket')
            owning_pocket = Pocket.objects.get(pocket_name = transaction_pocket, user_pocket = owninguser)
            if transaction.transaction_payment_type == 'Expense':
                owning_pocket.pocket_budget += int(transaction.transaction_amount)
                owning_pocket.save()
            else:
                owning_pocket.pocket_budget -= int(transaction.transaction_amount)
                owning_pocket.save()
            transaction.delete()
            return JsonResponse({'isSuccessful':True},safe = False)
        except Pocket.DoesNotExist or Account.DoesNotExist or Transaction.DoesNotExist:
            return JsonResponse({'isSuccessful':False},status=404,safe = False)



@csrf_exempt
def view_all_transaction(request):
    session_id = request.GET.get('session_id')
    engine = import_module(settings.SESSION_ENGINE)
    sessionstore = engine.SessionStore
    session = sessionstore(session_id)
    email = session.get('_auth_user_id')
    pocket = request.GET.get('input_pocketname')
    owninguser = Account.objects.get(email = email)
    alltransaction = Transaction.objects.filter(transaction_pocket = pocket)
    transaction_list = []
    for transaction in alltransaction:
        transaction_list.append({
            'transaction_payment_name' : transaction.transaction_payment_name,
            'transaction_amount' : formatrupiah(transaction.transaction_amount),
            'transaction_date' : str(transaction.transaction_date),
            'transaction_transaction_type' : transaction.transaction_transaction_type,
            'transaction_payment_type' : transaction.transaction_payment_type,
            'transaction_pocket' : transaction.transaction_pocket.pocket_name
        })
    data = json.dumps(transaction_list)
    return HttpResponse(data, content_type='application/json')
