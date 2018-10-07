from django.shortcuts import render, redirect, render_to_response
from customerapp.models import Customer
from dashboard.models import Request,CompleteRequest
import sys
import json
import datetime
# Create your views here.

def index(request):
	try:
		print("In try")
		reqs = []
		ride_requests = Request.objects.all()
		for ride in ride_requests:
			dt = datetime.datetime.now()
			dt = dt.replace(tzinfo=datetime.timezone.utc)
			time_elapsed = dt - ride.start_time
			time_elapsed = time_elapsed.total_seconds()/60
			print("Looke here")
			print(ride.driver)
			if(time_elapsed >= 5 and ride.driver != None):
				ride.status = 'completed'
				complete,created = CompleteRequest.objects.get_or_create(driver=ride.driver,request=ride)
				ride.save()	
		for ride in ride_requests:
			req = {}
			req['id'] = ride.id
			req['customer_id'] = ride.customer.customer_id
			dt = datetime.datetime.now()
			dt = dt.replace(tzinfo=datetime.timezone.utc)
			time_elapsed = dt - ride.start_time
			time_elapsed = time_elapsed.total_seconds()/60
			req['time_elapsed'] = int(time_elapsed)
			req['status'] = ride.status
			if(ride.driver != None):
				req['driver'] = ride.driver.id
			else:
				req['driver'] = ride.driver	
			reqs.append(req)
		print("End of loop")
		print(reqs)	
		return render(request, 'dashboard.html',{'ride_requests':reqs})	
	except Exception as e:
		print(str(e))
		print("Error")
		return json.dumps('error getting requests,Please try again')
