from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .models import Project, Resource, ResourceAllocation, Login, DateSave
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from datetime import datetime
from datetime import date
import calendar
from datetime import timedelta
from django.http import HttpResponse

# Create your views here.
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                Login(request, user)
                return redirect('http://127.0.0.1:8000/Home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "Login.html",
                    context={"form":form})

def show(request):
    return render(request,'Login.html')

def show2(request):
    return render(request,'ProjectWorkspace.html')

def show3(request):
    resourceallocation_obj = ResourceAllocation.objects.all()
    project_obj = Project.objects.all()
    resource_obj = Resource.objects.all()
    daydetail_obj = DateSave.objects.all()

    return render(request,'ProjectAllocator.html', {'resourceallocation_obj': resourceallocation_obj, 'n': range(1,32), 'project_obj': project_obj, 'resource_obj':resource_obj , 'day_details':daydetail_obj})

def show4(request):
    return render(request, 'ProjectResource.html')


def fetch(request):
    if (request.method == 'POST'):
        year = request.POST.get('ddlYears')
        month = request.POST.get('month')
        project_obj = Project.objects.all()
        resource_obj = Resource.objects.all()
        daydetail_obj = DateSave.objects.all()
        fetch_obj = ResourceAllocation.objects.filter(year = year, month = month)
    return render(request, 'ProjectAllocator.html',{'resourceallocation_obj': fetch_obj, 'n': range(1, 32),
                                                    'day_details': daydetail_obj,
                                                    'project_obj': project_obj, 'resource_obj': resource_obj })


def store(request):
    project = Project.objects.all()
    if (request.method == 'POST'):
        pro = Project()
        pro.id = request.POST.get('id')
        pro.ProjectName = request.POST.get('ProjectName')
        pro.Project_Description = request.POST.get('Project_Description')
        pro.Project_Department = request.POST.get('Project_Department')
        pro.StartDate_pro = request.POST.get('StartDate_pro')
        pro.EndDate_pro = request.POST.get('EndDate_pro')
        pro.save()
    return render(request, 'ShowProject.html', {'pro': project})

def store2(request):
    resource = Resource.objects.all()
    if(request.method == 'POST'):
        res = Resource()
        res.id = request.POST.get('id')
        res.ResourceName = request.POST.get('ResourceName')
        res.StartDate = request.POST.get('StartDate')
        res.EndDate = request.POST.get('EndDate')
        res.save()
    return render(request, 'ShowResource.html' ,{'res':resource})

def store3(request):
    if (request.method == 'POST'):
        resourceallocation_obj = ResourceAllocation()
        p_name = request.POST.get('ProjectName')
        project_obj = Project.objects.get(ProjectName=p_name)
        r_name = request.POST.get('ResourceName')
        resource_obj = Resource.objects.get(ResourceName=r_name)
        resourceallocation_obj.Project_id = project_obj
        resourceallocation_obj.Resource_id = resource_obj
        resourceallocation_obj.StartDate_all = request.POST.get('StartDate_all')
        resourceallocation_obj.EndDate_all = request.POST.get('EndDate_all')
        resourceallocation_obj.points = request.POST.get('points')
        s_date = datetime.strptime(resourceallocation_obj.StartDate_all, '%Y-%m-%d')
        e_date = datetime.strptime(resourceallocation_obj.EndDate_all, '%Y-%m-%d')
        resourceallocation_obj.StartDay_all = s_date.strftime("%d")
        resourceallocation_obj.month = s_date.strftime("%m")
        resourceallocation_obj.year = s_date.strftime("%Y")
        resourceallocation_obj.EndDay_all = e_date.strftime("%d")
        resourceallocation_obj.save()
        endate = calendar.monthrange(int(resourceallocation_obj.year), int(resourceallocation_obj.month))[1]  # Ex: 30/31/29
        ending_date = date(int(resourceallocation_obj.year), int(resourceallocation_obj.month), endate)  # Ex: 31-10-2021
        starting_date = date(int(resourceallocation_obj.year), int(resourceallocation_obj.month), int('1'))
        started_date = date(int(resourceallocation_obj.StartDate_all[0:4]), int(resourceallocation_obj.StartDate_all[5:7]),
                            int(resourceallocation_obj.StartDate_all[8:]))
        ended_date = date(int(resourceallocation_obj.EndDate_all[0:4]), int(resourceallocation_obj.EndDate_all[5:7]),
                          int(resourceallocation_obj.EndDate_all[8:]))
        def daterange(start_date, end_date):
            for n in range(int((end_date - start_date).days) + 1):
                yield start_date + timedelta(n)
        for single_date in daterange(starting_date, ending_date):
            daydetail_obj = DateSave()
            daydetail_obj.Allocation_id = resourceallocation_obj
            daydetail_obj.Day = single_date
            if single_date.strftime("%A") in ["Saturday", "Sunday"]:
                daydetail_obj.date = single_date
                daydetail_obj.day = single_date.strftime("%d")
                daydetail_obj.month = single_date.strftime("%m")
                daydetail_obj.year = single_date.strftime("%Y")
                daydetail_obj.day_week = single_date.strftime("%A")
                daydetail_obj.DayValue = ''
                daydetail_obj.save()
            else:
                daydetail_obj.date = single_date
                daydetail_obj.day = single_date.strftime("%d")
                daydetail_obj.month = single_date.strftime("%m")
                daydetail_obj.year = single_date.strftime("%Y")
                daydetail_obj.weekday = single_date.strftime("%A")
            if single_date >= started_date and single_date <= ended_date:
                daydetail_obj.DayValue = resourceallocation_obj.points
            else:
                daydetail_obj.DayValue = '0'
            daydetail_obj.save()
    resourceallocation_obj = ResourceAllocation.objects.all()
    daydetail_obj = DateSave.objects.all()
    pro = Project.objects.all()
    res = Resource.objects.all()
    return render(request, 'ProjectAllocator.html', {'resourceallocation_obj': resourceallocation_obj, 'resource_obj': res,
                   'project_obj': pro,  'day_details':daydetail_obj, 'n': range(1,32)})


def index_1(request):
    pro = Project.objects.all()
    return render(request, 'ProjectWorkspace.html',{'pro':pro})

def viewProject(request,pk):
   pro = Project.objects.get(P_ID = pk)
   return render(request, 'view.html',{'pro':pro})

def viewResource(request):
    res = Resource.objects.all()
    # return render(request, 'ShowResource.html')
    return render(request, 'ShowResource.html', {'res': res})


def deleteResource(request, pk):
    res = Resource.objects.get(id = pk)
    res.delete()

    res = Resource.objects.all()
    return render(request, 'ShowResource.html', {'res': res})

    # return redirect('/')

def deleteAllocation(request, pk):
    resourceallocation_obj = ResourceAllocation.objects.get(id = pk)
    resourceallocation_obj.delete()

    pro = Project.objects.all()
    res = Resource.objects.all()
    resourceallocation = ResourceAllocation.objects.all()
    daydetail_obj = DateSave.objects.all()
    return render(request, 'ProjectAllocator.html',
                  {'resourceallocation_obj': resourceallocation, 'resource_obj': res,
                   'project_obj': pro, 'n': range(1, 32) , 'day_details': daydetail_obj})


def updateView(request,pk):
    res = Resource.objects.get(id = pk)
    return render(request,'updateResource.html',{'res':res})

def update(request,pk):
    res = Resource.objects.get(id = pk)
    res.ResourceName = request.POST.get('ResourceName')
    res.StartDate = request.POST.get('StartDate')
    res.EndDate = request.POST.get('EndDate')
    res.save()
    res = Resource.objects.all()
    return render(request, 'ShowResource.html', {'res': res})

def updateViewAllocation(request,pk):
    resourceallocation_obj = ResourceAllocation.objects.get(id = pk)
    daydetail_obj = DateSave.objects.all()
    return render(request,'UpdateAllocation.html',{'resourceallocation_obj':resourceallocation_obj , 'day_details' :daydetail_obj } )

def UpdateAllocation(request,pk):
    if (request.method == 'POST'):
        resourceallocation_obj = ResourceAllocation.objects.get(id = pk)
        # project_obj = Resource.objects.get(Project_id=pk)
        # resource_obj = Resource.objects.get(Resource_id=pk)
        p_name = request.POST.get('ProjectName')
        project_obj = Project.objects.get(ProjectName=p_name)
        r_name = request.POST.get('ResourceName')
        resource_obj = Resource.objects.get(ResourceName=r_name)
        resourceallocation_obj.Project_id = project_obj
        resourceallocation_obj.Resource_id = resource_obj
        resourceallocation_obj.StartDate_all = request.POST.get('StartDate_all')
        resourceallocation_obj.EndDate_all = request.POST.get('EndDate_all')
        s_date = datetime.strptime(resourceallocation_obj.StartDate_all, '%Y-%m-%d')
        e_date = datetime.strptime(resourceallocation_obj.EndDate_all, '%Y-%m-%d')
        sdate = s_date.date()
        edate = e_date.date()
        resourceallocation_obj.points = request.POST.get('points')
        resourceallocation_obj.save()
        day_save = DateSave.objects.filter(Allocation_id = pk)
        for x in day_save:
            print(type(x.Day))
            if sdate <= x.Day <= edate:
                x.DayValue = resourceallocation_obj.points
                x.save()
    resourceallocation_obj = ResourceAllocation.objects.all()
    # k = [4, 6, 9, 11]
    project_obj = Project.objects.all()
    resource_obj = Resource.objects.all()
    daydetail_obj = DateSave.objects.all()
    return render(request, 'ProjectAllocator.html', {'resourceallocation_obj': resourceallocation_obj,
                                                     'resource_obj': resource_obj,
                                                     'project_obj': project_obj, 'n': range(1, 32),
                                                     'day_details': daydetail_obj
                                                     })


def deleteProject(request, pk):
    pro = Project.objects.get(id = pk)
    type(pro)
    pro.delete()
    pro = Project.objects.all()
    return render(request, 'ShowProject.html', {'pro': pro})

    # return redirect('/')

def updateViewProject(request,pk):
    pro = Project.objects.get(id = pk)
    return render(request,'UpdateProject.html',{'pro':pro})


def updateProject(request,pk):
    print('in')
    pro = Project.objects.get(id = pk)
    pro.ProjectName = request.POST.get('ProjectName')
    pro.Project_Description = request.POST.get('Project_Description')
    pro.Project_Department = request.POST.get('Project_Department')
    pro.save()
    pro = Project.objects.all()
    return render(request, 'ShowProject.html', {'pro': pro})

def showProjectlist(request):
    result2 = Project.objects.all()
    return render(request, "ProjectAllocator.html", {"projectlist": result2})

def showResourcelist(request):
    result1 = Resource.objects.all()
    return render(request, "ProjectAllocator.html", {"resourcelist": result1})

