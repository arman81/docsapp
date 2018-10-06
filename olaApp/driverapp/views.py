from django.shortcuts import render
from dashboard.models import Request,CompleteRequest
from driverapp.models import Driver

# Create your views here.
def get_driver_panel(request,id):
	try:
		waiting = Request.objects.filter(status='waiting')
		driver = Driver.objects.get(id=id)
		ongoing = Request.objects.filter(status='ongoing',driver=driver)
		completed = CompleteRequests.objects.get(driver=driver_detail)
		return render(request, 'driver_panel.html',{'waiting':waiting,'driver_detail':driver_detail,'complete':completed})
	except Exception as e:
		return render(request, 'driver_panel.html')

def select_ride(request):
	try:
		request_id = request.POST['ride_id']
		driver_id = request.POST['driver_id']
		driver = Driver.objects.get(id=driver_id)
		request = Request.objects.get(id=request_id)
		if(request.status != 'waiting'):
			return json.dumps('Ride Not available')
		else:
			request.status = 'ongoing'
			request.driver = driver
			request.save()
			return json.dumps('success')
	except Exception as e:
		return json.dumps({'error':error})
		