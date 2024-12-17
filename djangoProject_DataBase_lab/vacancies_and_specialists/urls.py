from django.urls import path

from vacancies_and_specialists import views

urlpatterns=[
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('loginemployee/',views.login_Employee,name='login_Employee'),
    path('loginemployer/',views.login_Employer,name='login_Employer'),
    path('employer/<slug:slug_employer>',views.employer,name='employer'),
    path('employee/<slug:slug_employee>', views.employee, name='employee'),
    # path('job/',views.job,name='job'),
    path('job/<slug:slug_job>',views.job_slug,name='job_slug'),
    path('workers/',views.workers,name='workers'),
    path('changing_employee/<slug:slug_employee>',views.changing_employee,name='changing_employee'),
    path('employers/',views.list_employers,name='list_employers'),
    path('changing_employer/<slug:slug_employer>',views.changing_employer,name='changing_employer'),
    path('list_specialities/',views.list_specialities,name='list_specialities'),
    # path('worker/delete/<slug:worker_slug>/',views.delet_worker,name='delet_worker'),

]