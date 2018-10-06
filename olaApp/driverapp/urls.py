from django.conf.urls import url, include

from driverapp import views

urlpatterns = [
	url(r'driverapp.html/(?P<id>\d+)/$',views.get_driver_panel,name='get_driver_panel'),
	url(r'select_ride/$',views.select_ride,name='select_ride'),
]