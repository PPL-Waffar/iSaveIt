from cmath import exp
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from importlib import import_module
from django.conf import settings
from expense.models import Expense
from payment.models import Payment
from pocket.models import Pocket
from transaction.models import Transaction
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
    total_amount = 0
    expenses = Expense.objects.filter(user_expense = owninguser)
    for expense in expenses:
        total_amount += expense.expense_amount

    total_income = 0
    pockets = Pocket.objects.filter(user_pocket = owninguser)
    for pocket in pockets:
        total_income += pocket.pocket_budget
    transactions = Transaction.objects.filter(user_transaction = owninguser)
    
    payments = Payment.objects.filter(user_payment = owninguser)

    expenses = Expense.objects.filter(user_expense = owninguser)
    dict1 = dict.fromkeys(['01', '02', '03', '04','05','06','07','08','09','10','11','12'])
    expense_list = []
    total_income = 0
    for key in dict1:
        dict1[key] = []
    for key in dict1:
        total_amount = 0
        total_income = 0
        for expense in expenses:
            if str(expense.expense_date)[5:7] == str(key) :
                total_amount += expense.expense_amount
                dict1[key].append({'expense_name' : expense.expense_name,
            'expense_amount' : formatrupiah(expense.expense_amount),
            'expense_nilai' : expense.expense_amount,
            'expense_date' : str(expense.expense_date),
            'total_amount' : formatrupiah(total_amount),
            'total_income' : formatrupiah(total_income),
            })
        for transaction in transactions:
            if str(transaction.transaction_date)[5:7] == str(key) :
                if transaction.transaction_payment_type == 'Expense':
                    total_amount += transaction.transaction_amount
                    dict1[key].append({'expense_name' : transaction.transaction_payment_name,
                'expense_amount' : formatrupiah(transaction.transaction_amount),
                'expense_nilai' : transaction.transaction_amount,
                'expense_date' : str(transaction.transaction_date),
                'total_income' : formatrupiah(total_income),
                'total_amount' : formatrupiah(total_amount),})
                if transaction.transaction_payment_type == 'Income':
                    total_income += transaction.transaction_amount
                    dict1[key].append({
                'expense_name' : transaction.transaction_payment_name,
                'expense_amount' : formatrupiah(transaction.transaction_amount),
                'expense_nilai' : transaction.transaction_amount,
                'expense_date' : str(transaction.transaction_date),
                'total_amount' : formatrupiah(total_amount),
                'total_income' : formatrupiah(total_income),})
        for payment in payments:
            if str(payment.pay_date)[5:7] == str(key) :
                total_amount += payment.pay_amount
                dict1[key].append({
            'expense_name' : payment.pay_name,
            'expense_amount' : formatrupiah(payment.pay_amount),
            'expense_nilai' : payment.pay_amount,
            'expense_date' : str(payment.pay_date),
            'total_amount' : formatrupiah(total_amount),
            'total_income' : formatrupiah(total_income),})
    
    return JsonResponse({'total_amount': json.dumps(formatrupiah(total_amount)), 'total_income':json.dumps(formatrupiah(total_income)), 'expense_list':json.dumps(dict1)}, content_type="application/json")
