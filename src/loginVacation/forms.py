from django.forms import ModelForm
from django import forms
import datetime

class EmployeeForm(forms.Form):
    startVacation = forms.DateField(
        widget=forms.SelectDateWidget(),
        initial = datetime.datetime.now()
    )

    endVacation = forms.DateField(
        widget=forms.SelectDateWidget(),
        initial = datetime.datetime.now() + datetime.timedelta(days=4)
    )
