from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from importlib import import_module
from django.conf import settings
from expense.models import Expense
from pocket.models import Pocket
from payment.models import Payment
from user.models import *
import json
from django.http.response import  JsonResponse
from django.views.decorators.http import require_http_methods

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
        expenses = Expense.objects.filter(user_expense = owninguser)
        expense_list = []
        for expense in expenses:
            expense_list.append({
                "expense_name" : expense.expense_name,
                "expense_amount" : expense.expense_amount,
                "expense_date" : expense.expense_date,
                "expense_type" : expense.expense_type,
                "expense_person" : expense.expense_person,
                "expense_payment_choice" : expense.expense_payment_choice,
                "expense_pocket" : expense.expense_pocket,
            })
        return JsonResponse(expense_list,safe = False)

@require_http_methods(["POST"])
@csrf_exempt
#Create add expense
def add_expense(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        engine = import_module(settings.SESSION_ENGINE)
        sessionstore = engine.SessionStore
        session = sessionstore(session_id)
        email = session.get('_auth_user_id')
        owninguser = Account.objects.get(email = email)
        expense_name = request.POST.get('expense_name')
        expense_amount = request.POST.get('expense_amount')
        expense_date = request.POST.get('expense_date')
        expense_type = request.POST.get('expense_type')
        expense_person = request.POST.get('expense_person')
        expense_payment_choice = request.POST.get('expense_payment_choice')
        expense_pocket = request.POST.get('expense_pocket')
        expense = Expense(user_expense = owninguser, expense_name = expense_name, expense_amount = expense_amount, expense_date = expense_date, expense_type = expense_type, expense_person = expense_person, expense_payment_choice = expense_payment_choice, expense_pocket = expense_pocket)
        expense.save()
        return JsonResponse({"status" : "success"})
