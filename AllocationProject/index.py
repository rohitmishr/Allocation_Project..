from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

def show(request):
    return render(request, 'Login.html')

def show1(request):
    return render(request, 'Home.html')

def show2(request):
    return render(request, 'ProjectWorkspace.html')

def show3(request):
    return render(request,'ProjectAllocator.html')

def show4(request):
    return render(request,'ProjectResource.html')

def ShowResource(request):
    return render(request,'ShowResource.html')

