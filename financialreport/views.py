from cmath import exp
from django.views.decorators.csrf import csrf_exempt
from importlib import import_module
from django.conf import settings
from expense.models import Expense
from pocket.models import Pocket
from user.models import Account
import json
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
@csrf_exempt
def view_financial_report(request):
    if request.method == 'GET':
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
        expense_list = []
        for expense in expenses:
            expense_list.append({
                'expense_name' : expense.expense_name,
                'expense_amount' : expense.expense_amount,
                'expense_date' : expense.expense_date
            })
        expense_list.sort(key = lambda x: x['expense_date'], reverse = True)
        for expense in expense_list:
            del expense['expense_date']
        
        return JsonResponse({'total_expense':total_expense, 'total_income':total_income, 'expense_list':expense_list}, safe = False)
