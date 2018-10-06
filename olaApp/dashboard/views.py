from django.shortcuts import render, redirect, render_to_response
from customerapp.models import Customer
from dashboard.models import Request
import sys
import json
import datetime
# Create your views here.

def index(request):
	try:
		print("In try")
		reqs = []
		requests = Request.objects.all()
		# for request in requests:
		# 	time_elapsed = datetime.now() - request.start_time
		# 	time_elapsed = time_elapsed.total_seconds()/60
		# 	if(time_elapsed >= 5):
		# 		request.status = 'completed'
		# 		request.save()
		print("Beech mein hai")		
		for request in requests:
			req = {}
			req['id'] = request.id
			req['cusomter_id'] = request.customer
			time_elapsed = request.start_time
			# time_elapsed = time_elapsed.total_seconds()/60
			req['time_elapsed'] = time_elapsed
			req['status'] = request.status
			req['driver'] = request.driver
			reqs.append(req)
		print("End of loop")
		print(reqs)	
		return render(request, 'dashboard.html',{'requests':reqs})	
	except Exception as e:
		print(str(e))
		print("Error")
		return json.dumps('error getting requests,Please try again')
