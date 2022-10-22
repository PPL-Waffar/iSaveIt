from cmath import exp
from django.views.decorators.csrf import csrf_exempt
from importlib import import_module
from django.conf import settings
from expense.models import Expense
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
        total_expense = json.loads(Expense.total_expense(request).content)
        total_expense = total_expense.get('total_expense')
        expense_list = json.loads(Expense.view_expense(request).content)
        expense_list = [expense_list]
        return JsonResponse({'total_expense':total_expense,'expense_list':expense_list},safe = False)
