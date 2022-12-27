from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from importlib import import_module
from django.conf import settings
from expense.models import Expense
from pocket.models import Pocket
from user.models import Account
import json
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods

def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3 :
        return 'Rp ' + y     
    else :
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p
@require_http_methods(["GET"])
@csrf_exempt
def view_expense(request):
    if request.method == 'GET':
        session_id = request.GET.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        owninguser = Account.objects.get(email = email)
        pocket_expense = Pocket.objects.get(user_pocket = owninguser)
        expenses = Expense.objects.filter(user_expense = owninguser)
        expense_list = []
        for expense in expenses:
            expense_list.append({
                'expense_name' : expense.expense_name,
                'expense_amount' : expense.expense_amount,
                'expense_date' : expense.expense_date,
                'expense_category' : expense.expense_type,
                'expense_person' : expense.expense_person,
                'expense_payment_choice' : expense.expense_payment_choice,
                'expense_pocket' : pocket_expense.pocket_name,
            })
        return JsonResponse(expense_list,safe = False)

@require_http_methods(["POST"])
@csrf_exempt
def add_expense(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        session_id = data.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        owninguser = Account.objects.get(email = email)
        expense_name = data.get('expense_name')
        expense_amount = data.get('expense_amount')
        expense_date = data.get('expense_date')
        expense_type = data.get('expense_type')
        expense_person = data.get('expense_person')
        expense_payment_choice = data.get('expense_payment_choice')
        expense_pocket = data.get('expense_pocket')
        pocket = Pocket.objects.get(pocket_name = expense_pocket)
        if expense_type == 'Lend Money':
            pocket.pocket_budget -= int(expense_amount)
            pocket.save()
        else:
            pocket.pocket_budget += int(expense_amount)
            pocket.save()
        expense = Expense(user_expense = owninguser, expense_name = expense_name, expense_amount = expense_amount, expense_date = expense_date, expense_type = expense_type, expense_person = expense_person, expense_payment_choice = expense_payment_choice, expense_pocket = pocket)
        
        expense.save()
    return JsonResponse({'isSuccessful':True},safe = False)

@require_http_methods(["GET"])
@csrf_exempt
def total_expense(request):
    if request.method == 'GET':
        session_id = request.GET.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        owninguser = Account.objects.get(email = email)
        expenses = Expense.objects.filter(user_expense = owninguser)
        total_expense = 0
        for expense in expenses:
            total_expense += expense.expense_amount
        return JsonResponse({'total_expense':total_expense},safe = False)
    
@csrf_exempt
def get_expense(request):
    session_id = request.GET.get('session_id')
    engine = import_module(settings.SESSION_ENGINE)
    sessionstore = engine.SessionStore
    session = sessionstore(session_id)
    email = session.get('_auth_user_id')
    owninguser = Account.objects.get(email = email)
    expenses = Expense.objects.filter(user_expense = owninguser)
    expense_list = []
    for expense in expenses:
        expense_list.append({
            'expense_name' : expense.expense_name,
            'expense_amount' : formatrupiah(expense.expense_amount),
            'expense_date' : str(expense.expense_date),
            'expense_category' : expense.expense_type,
            'expense_person' : expense.expense_person,
            'expense_payment_choice' : expense.expense_payment_choice,
        })
    return HttpResponse(json.dumps(expense_list), content_type="application/json")
