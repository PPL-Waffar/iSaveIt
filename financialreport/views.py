from cmath import exp
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

@csrf_exempt
def view_financial_report(request):
    session_id = request.GET.get('session_id')
    engine = import_module(settings.SESSION_ENGINE)
    sessionstore = engine.SessionStore
    session = sessionstore(session_id)
    email = session.get('_auth_user_id')
    owninguser = Account.objects.get(email = email)
    total_expense = 0
    expenses = Expense.objects.filter(user_expense = owninguser)
    for expense in expenses:
        total_expense += expense.expense_amount

    total_income = 0
    pockets = Pocket.objects.filter(user_pocket = owninguser)
    for pocket in pockets:
        total_income += pocket.pocket_budget

    expenses = Expense.objects.filter(user_expense = owninguser)
    dict1 = dict.fromkeys(['01', '02', '03', '04','05','06','07','08','09','10','11','12'])
    expense_list = []
    
    for key in dict1:
        dict1[key] = []
    for expense in expenses:
        for key in dict1:
            if str(expense.expense_date)[5:7] == str(key) :
                dict1[key].append({'expense_name' : expense.expense_name,
            'expense_amount' : formatrupiah(expense.expense_amount),
            'expense_date' : str(expense.expense_date)})
    
    return JsonResponse({'total_expense': json.dumps(total_expense), 'total_income':json.dumps(total_income), 'expense_list':json.dumps(dict1)}, content_type="application/json")
