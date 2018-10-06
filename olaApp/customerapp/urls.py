from django.conf.urls import url, include

from customerapp import views

urlpatterns = [
	url(r'^customerapp.html', views.index, name='home'),
]
