from django.shortcuts import render
from dashboard.models import Request,CompleteRequest
from driverapp.models import Driver
import json
# Create your views here.
def get_driver_panel(request,id):
	if request.method == 'GET':	
		try:
			print(id)
			waiting = Request.objects.filter(status='waiting')
			print(waiting)
			driver = Driver.objects.get(id=id)
			ongoing = Request.objects.filter(status='ongoing',driver=driver)
			#completed = CompleteRequests.objects.get(driver=driver_detail)
			ongoing = []
			completed = []
			return render(request, 'driverApp.html',{'waiting':waiting,'ongoing':ongoing,'complete':completed,'id':id})
		except Exception as e:
			print("ERror")
			print(str(e))
			return render(request, 'driverApp.html')
	else:
		try:
			print("Got Request")
			request_id = request.POST['req_id']
			print("Got request_id")
			driver_id = request.POST['driver_id']
			print(request_id)
			print(driver_id)
			driver = Driver.objects.get(id=driver_id)
			request = Request.objects.get(id=request_id)
			print("In between request")
			if(request.status != 'waiting'):
				return HttpResponse(json.dumps('Ride not available'))
			else:
				print("In else")
				request.status = 'ongoing'
				request.driver = driver
				request.save()
				print("ride assign complete")
				return HttpResponse(json.dumps('Ride taken SuccessFully'))
		except Exception as e:
			return json.dumps({'error':str(e)})

		