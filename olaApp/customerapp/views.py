from django.shortcuts import render, redirect, render_to_response
from customerapp.models import Customer
from dashboard.models import Request
from customerapp.forms import RequestAddForm
import datetime
import sys
import json
# Create your views here.

def index(request):
	if request.method == 'POST':
		try:
			form = RequestAddForm(request.POST)
			if form.is_valid():
				customer_id = form.cleaned_data['customer_id']
				customer,created  = Customer.objects.get_or_create(customer_id=customer_id)
				Request.objects.create(customer=customer,
									start_time=datetime.datetime.now(),
									status='waiting')
			form_new = RequestAddForm()
			print('Now returning HttpResponse')
			return render(request, 'customerApp.html',{'form':form_new,'added':1})	
		except Exception as e:
			raise e
			return render(request, 'customerApp.html',{'error':1})
	else:
		print("In else")
		form = RequestAddForm()
		return render(request, 'customerApp.html',{'form':form})
				
