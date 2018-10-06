from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'olaApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('dashboard.urls')),
    url(r'', include('customerapp.urls')),
    url(r'', include('driverapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
