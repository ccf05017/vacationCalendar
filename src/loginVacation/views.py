from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import AuthEmployee
from calendarModule.models import Employee
from .forms import EmployeeForm
import datetime
from datetime import timedelta


# Create your views here.
def loginVacation(request):

    if request.method == "GET":
        pass

    elif request.method == "POST":
        employeenumber = request.POST.get("employeenumber")
        password = request.POST.get("password")
        user = authenticate(username=employeenumber, password=password)
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

    vacation_form = EmployeeForm()

    context = {
        "vacation_form" : vacation_form
    }

    if request.method == "GET":
        pass

    elif request.method == "POST":
        # employee model로 넘기기 위한 기본 값들 받음
        employeeNumber = request.user.username
        department = request.user.authemployee.department
        realName = request.user.authemployee.realName

        # employee model로 보내기 위한 날짜 계산
        startVacationYear = int(request.POST.get("startVacation_year"))
        startVacationMonth = int(request.POST.get("startVacation_month"))
        startVacationDay = int(request.POST.get("startVacation_day"))
        endVacationYear = int(request.POST.get("endVacation_year"))
        endVacationMonth = int(request.POST.get("endVacation_month"))
        endVacationDay = int(request.POST.get("endVacation_day"))
        startVacation = datetime.date(
            startVacationYear, startVacationMonth, startVacationDay
        )
        endVacation = datetime.date(
            endVacationYear, endVacationMonth, endVacationDay
        )

        # 기간을 각각의 일자로 만들어서 넘기기 위한 delta값 생성
        delta = endVacation - startVacation

        for i in range(delta.days + 1):
            employee = Employee.objects.create_employee(
                int(employeeNumber),
                realName,
                department,
                startVacation+timedelta(days=i))

            employee.save()

        return redirect("completeInput")

    return render(request, "inputVacation.html", context)

def completeInput(request):
    context = {

    }
    logout(request)
    return render(request, "completeInput.html", context)
