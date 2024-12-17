from cProfile import label

from django import forms
from django.core.validators import RegexValidator

from vacancies_and_specialists.procedures import get_all_specialities


class EmployerForm(forms.Form):
    name = forms.CharField(max_length=255, label='Название компании',required=True,validators=[RegexValidator(
            regex='^[a-zA-Z0-9]*$',  # Разрешает только латинские буквы и цифры
            message='Введите только латинские буквы и цифры.'
        )])
    location = forms.CharField(max_length=255, label='Город где находится оффис',required=True)
    contact_info = forms.CharField(max_length=255, label='Контактная информация',required=True)
    job_title = forms.CharField(max_length=255, label='Название работы',required=True,validators=[RegexValidator(
            regex='^[a-zA-Z0-9]*$',  # Разрешает только латинские буквы и цифры
            message='Введите только латинские буквы и цифры.'
        )])
    job_description = forms.CharField(widget=forms.Textarea, label='Описание',required=True)
    job_location = forms.CharField(max_length=255, label='Город куда требуется сотрудник',required=True)
    job_salary = forms.DecimalField(max_digits=15, decimal_places=2, label='Зарплата',required=True)
class JobForm(forms.Form):
    job_title = forms.CharField(max_length=255, label='Название работы',required=True,validators=[RegexValidator(
            regex='^[a-zA-Z0-9]*$',  # Разрешает только латинские буквы и цифры
            message='Введите только латинские буквы и цифры.'
        )])
    job_description = forms.CharField(widget=forms.Textarea, label='Описание',required=True)
    job_location = forms.CharField(max_length=255, label='Город куда требуется сотрудник',required=True)
    job_salary = forms.DecimalField(max_digits=15, decimal_places=2, label='Зарплата',required=True)
# forms.py

class JobSearchForm(forms.Form):
    query = forms.CharField(max_length=100 ,label="Поиск по названию работы")
class EmployeeForm(forms.Form):
    first_name = forms.CharField(max_length=255, label='Имя',required=True,validators=[RegexValidator(
            regex='^[a-zA-Z0-9]*$',  # Разрешает только латинские буквы и цифры
            message='Введите только латинские буквы и цифры.'
        )])
    last_name = forms.CharField(max_length=255, label='Фамилия', required=True,validators=[RegexValidator(
            regex='^[a-zA-Z0-9]*$',  # Разрешает только латинские буквы и цифры
            message='Введите только латинские буквы и цифры.'
        )])
    position= forms.CharField(max_length=255, label='Ваша позиция',required=True)
    contact_info = forms.CharField(max_length=255, label='Контактная информация',required=True)
    specialities=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=get_all_specialities(),label='Специализация')

class WorkerSearchForm(forms.Form):
    query = forms.CharField(max_length=100, label="Поиск по названию работы")