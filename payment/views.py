from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from importlib import import_module
from django.conf import settings
from .models import *
import json
from django.http.response import HttpResponse, HttpResponseForbidden, JsonResponse
# Create your views here.
from django.views.decorators.http import require_http_methods
@csrf_exempt
@require_http_methods(["POST"])
def flutter_add_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        pay_name = data.get('input_payname')
        pay_amount = data.get('input_payamount')
        pay_date = data.get('input_paydate')
        pay_categories = data.get('input_paycategories')
        payment_choice = data.get('input_paymentchoice')
        new_payment = Payment(pay_name = pay_name, pay_date = pay_date, pay_amount= pay_amount, pay_categories=pay_categories, payment_choice =payment_choice)
        new_payment.save()
    return JsonResponse({'isSuccessful':True},safe = False)

