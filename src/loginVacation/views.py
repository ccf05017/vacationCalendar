from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import AuthEmployee

# Create your views here.
def loginVacation(request):

    if request.method == "GET":
        pass

    elif request.method == "POST":
        employeenumber = request.POST.get("employeenumber")
        password = request.POST.get("password")
        print(employeenumber)
        print(password)
        user = authenticate(username=employeenumber, password=password)
        print(user)
        if user is not None:
            # login success case
            login(request, user)
            return redirect("inputVacation")
        else:
            # login fail case
            print("fail")
    context = {

    }
    return render(request, "login.html", context)

def inputVacation(request):
    if request.method == "GET":
        pass

    elif request.method == "POST":
        year = request.POST.get("year")
        month = request.POST.get("month")
        startDate = request.POST.get("startDate")
        endDate = request.POST.get("endDate")
        employeeNumber = request.user.username
        employeeName = request.user.authemployee.realName

    context = {

    }
    return render(request, "inputVacation.html", context)
