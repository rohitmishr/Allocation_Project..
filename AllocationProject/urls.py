"""AllocationProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from AllocationApp import views
from . import index
from django.views.generic.base import TemplateView
# from .views import login, storelogin
# from AllocationApp.views import viewProject


urlpatterns = [
    path('admin/', admin.site.urls),
    path("Login", views.login_request, name="Login"),
    path('', index.show, ),
    path('Home', index.show1,),
    path('ProjectWorkspace', index.show2,),
    # path('ProjectAllocator', index.show3, ),
    path('ProjectResource', views.show4, ),
    # path('Login', views.storelogin, ),
    path('store', views.store, name = 'store', ),
    #path('store2', views.store2, name = 'store2', ),
    path('/g', views.index_1),
    path('view/<int:pk>', views.viewProject,name='viewProject'),
    path('view_1/<int:pk>', views.viewResource,name='viewResource'),
    path('ShowResource', views.store2, name = 'store2'),
    # path('ProjectAllocator', views.store3, name = 'store3'),
    path('ShowProject', views.store, name = 'store'),
    path('delete/<int:pk>',views.deleteResource,name='deleteResource'),
    path('update/<int:pk>',views.updateView, name='updateView'),
    path('edit/<int:pk>',views.update, name='edit'),
    path('delete1/<int:pk>',views.deleteProject,name='deleteProject'),
    path('update1/<int:pk>',views.updateViewProject, name='updateViewProject'),
    path('edit1/<int:pk>',views.updateProject, name='edit1'),
    path('store3', views.store3, name = 'store3' ),
    path('ProjectAllocator', views.show3, name = 'ProjectAllocator' ),
    path('fetch', views.fetch, name = 'fetch'),
    # path('ProjectAllocator', views.fetch, name = 'ProjectAllocator'),
    path('deleteAllocation/<int:pk>',views.deleteAllocation,name='deleteAllocation'),
    path('edit2/<int:pk>',views.UpdateAllocation, name='edit2'),
    path('update2/<int:pk>',views.updateViewAllocation, name='updateViewAllocation'),
]
