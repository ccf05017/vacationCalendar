from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import Employee
from calendar import HTMLCalendar
from datetime import date
from itertools import groupby
from django.core.mail import send_mail
from loginVacation.models import AuthEmployee
from django.contrib.auth.models import User
import json
#import serializers

class VacationCalendar(HTMLCalendar):

    def __init__(self, vacations):
        super(VacationCalendar, self).__init__()
        self.vacations = self.group_by_day(vacations)

    def group_by_day(self, vacations):
        field = lambda vacation: vacation.vacationDate.day
        return dict (
            [(day, list(items)) for day, items in groupby(vacations, field)]
        )

    def formatday(self, day, weekday):
        # 날짜 내용이 있는 경우를 반환
        if day !=0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += 'today'
            if day in self.vacations:
                #cssclass += 'filled'
                body = ['<div>']
                num_nw=0
                num_svr=0
                for vacation in self.vacations[day]:
                    # 확인용 소스
                    # body.append(vacation.name)
                    # body.append('<br>')
                    # 마우스 오버했을 때 객체 보이게 할 것, 색 조절할 것
                    if vacation.department == 'nw':
                        num_nw += 1
                    if vacation.department == 'sr':
                        num_svr += 1
                body.append('<div class="vacationNW">NW: ' + str(num_nw) +
                    '</div>' )
                body.append('<div class="vacationSVR">SVR: ' + str(num_svr) +
                    '</div>')
                body.append('</div>')
                return self.day_cell(day, cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(day, cssclass, day)

        # day == 0일 경우, 공백을 반환
        return self.day_cell(day, 'noday', '&nbsp')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(VacationCalendar, self).formatmonth(year, month)

    def day_cell(self, day, cssclass, body):
        return '<td id="day%s" class="%s">%s</td>' % (day, cssclass, body)

# Create your views here.
def viewCalendar(request, year, month):
    employee_vacations = Employee.objects.order_by('vacationDate').filter(
        vacationDate__year = int(year), vacationDate__month = int(month)
    )
    result_calendar = VacationCalendar(employee_vacations).formatmonth(int(year), int(month))

    context = {
        'calendar': mark_safe(result_calendar),
        'employee': json.dumps([item.as_dict() for item in employee_vacations]),
        #'employee': [item.as_dict() for item in employee_vacations]
    }

    return render(request, "viewCalendar.html", context)

def noAnswer(request):
    # 모델들 로딩
    authEmployee_list = User.objects.all()
    employee_list = Employee.objects.all()
    noanswer_list = []
    noanswer_result_list = []

    # 두 모델을 비교
    # 입력된 휴가 일자가 5일 미만일 경우 noanswer_list에 추가
    for authemployee in authEmployee_list:
        inputVacationNum = 0
        for employee in employee_list:
            if str(authemployee.username) == str(employee.employeeNumber):
                inputVacationNum += 1
        if inputVacationNum != 5:
            noanswer_list.append(authemployee.username)

    # 관리자는 어차피 대상이 아니기 때문에 삭제해준다.
    noanswer_list.remove('admin')

    # 미응답자만 별도 list 관리
    for noanswer in noanswer_list:
        noanswer_result_list.append(User.objects.get(username=str(noanswer)))

    context = {
        "noanswer_result_list" : noanswer_result_list
    }
    return render(request, "noAnswer.html", context)
