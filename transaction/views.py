from importlib import import_module
import json

from user.models import Account
from .models import Pocket
from .models import Transaction
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings

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
            owning_pocket.pocket_balance -= transaction_amount
        else:
            owning_pocket.pocket_balance += transaction_amount
        
        new_transaction = Transaction(user_transaction = owninguser, transaction_payment_name = transaction_payment_name, 
                                        transaction_amount = transaction_amount, transaction_date = transaction_date, 
                                        transaction_transaction_type = transaction_transaction_type, 
                                        transaction_payment_type = transaction_payment_type, transaction_pocket = owning_pocket)
        new_transaction.save()
    return JsonResponse({'isSuccessful':True},safe = False)
