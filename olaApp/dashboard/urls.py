from django.conf.urls import url, include

from dashboard import views

urlpatterns = [
	url(r'^dashboard.html', views.index, name='home'),
]
