from django.contrib import admin
from dashboard.models import Request,CompleteRequest
# Register your models here.
admin.site.register(Request)
admin.site.register(CompleteRequest)