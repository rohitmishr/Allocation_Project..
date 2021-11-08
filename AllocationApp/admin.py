from django.contrib import admin

# Register your models here.
from . models import Project, Resource, ResourceAllocation, Login
admin.site.register(Project)
admin.site.register(Resource)
admin.site.register(ResourceAllocation)
admin.site.register(Login)
