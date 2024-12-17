from django.shortcuts import render, redirect

from vacancies_and_specialists.forms import EmployerForm, JobSearchForm, EmployeeForm, WorkerSearchForm, \
    JobForm
from vacancies_and_specialists.procedures import add_employer, get_jobs_and_employers, search_jobs_by_title, get_jobs, \
    search_job_by_slug_with_employer, assign_jobs_to_worker, get_workers, get_all_specialities, \
    get_worker_details_by_slug, delete_worker_by_slug, update_worker_and_specialities, get_all_employers, \
    get_employer_and_jobs_by_slug, delete_employer_and_jobs_by_slug, add_job_to_employer_by_slug, delete_job_by_slug, \
    get_specialities


def index(request):
    return render(request,'vacancies_and_specialists/index.html')
def main(request):
    if request.method == 'POST':
        query=JobSearchForm(request.POST)
        if(query.is_valid()):
            # jobs =get_jobs_and_employers()
            search=query.cleaned_data['query']
            jobs=search_jobs_by_title(search)
            # print(search_jobs_by_title(search))
            return render(request, 'vacancies_and_specialists/main.html', {'jobs':jobs, 'query': query})
            # print(search_jobs_by_title(search))
    else:
        query=JobSearchForm()
        jobs=get_jobs_and_employers()
    return render(request,'vacancies_and_specialists/main.html',{'jobs':jobs,'query':query})
def login_Employee(request):
    if request.method == "POST":
            employeee=EmployeeForm(request.POST)

            if employeee.is_valid():
                selected_jobs = request.POST.getlist('jobs')
                assign_jobs_to_worker(
                    employeee.cleaned_data['first_name'],
                    employeee.cleaned_data['last_name'],
                    employeee.cleaned_data['position'],
                    employeee.cleaned_data['contact_info'],
                    employeee.cleaned_data['specialities']
                )
                c=employeee.cleaned_data['specialities']
                # print(c)
                return redirect('main')
            # return redirect('main')
    else:
        employeee= EmployeeForm()
        # specialities=get_all_specialities()
        # print(jobs)
    data = {'employeee':employeee}
    return render(request,'vacancies_and_specialists/login_Employee.html',data)
def login_Employer(request):
    if request.method == "POST":
        employerr = EmployerForm(request.POST)
        if employerr.is_valid():
            add_employer(
                employerr.cleaned_data['name'],
                employerr.cleaned_data['location'],
                employerr.cleaned_data['contact_info'],
                employerr.cleaned_data['job_title'],
                employerr.cleaned_data['job_description'],
                employerr.cleaned_data['job_location'],
                employerr.cleaned_data['job_salary'],
            )
            return redirect('main')
    else:
        employerr = EmployerForm()
    data = {'employerr': employerr}
    return render(request, 'vacancies_and_specialists/login_Employer.html', data)
def workers(request):
    workers=get_workers()
    return render(request,'vacancies_and_specialists/employee.html',{'workers':workers})
def employer(request,slug_employer):
    if(request.method == "POST"):
        delete_employer_and_jobs_by_slug(slug_employer)
        return redirect('list_employers')
    else:
        employers_data=get_employer_and_jobs_by_slug(slug_employer)
        job_ref=[(employers_data[0][4][i],employers_data[0][5][i]) for i in range(len(employers_data[0][4]))]
        slug=employers_data[0][3]
        # print(employers_data)

    return render(request,'vacancies_and_specialists/employers_detail.html',{'employers':employers_data,'slug':slug,'job_ref':job_ref})
def employee(request,slug_employee):
    if (request.method == "POST"):
        delete_worker_by_slug(slug_employee)
        return redirect('workers')
    worker_data = get_worker_details_by_slug(slug_employee),

    worker = {
        'employee_id': worker_data[0][0][0],
        'first_name': worker_data[0][0][1],
        'last_name': worker_data[0][0][2],
        'position': worker_data[0][0][3],
        'contact_info': worker_data[0][0][4],
        'slug_employer': worker_data[0][0][5],
        'speciality_titles': worker_data[0][0][6],
    }
    # print(worker_data[0][0][5])
    return render(request, 'vacancies_and_specialists/employee_detail.html', {'worker': worker})


def job_slug(request,slug_job):
    if(request.method=="POST"):
        delete_job_by_slug(slug_job)
        return redirect('main')
    else:
        data={
            'job':search_job_by_slug_with_employer(slug_job),
        }
    # print(data['job'])
    return render(request,'vacancies_and_specialists/job_detail.html',data)
def changing_employee(request,slug_employee):
    if(request.method == "POST"):
        employeee = EmployeeForm(request.POST)
        if employeee.is_valid():
            print(employeee.cleaned_data['specialities'])
            update_worker_and_specialities(slug_employee,
                                           employeee.cleaned_data['first_name'],
                                           employeee.cleaned_data['last_name'],
                                           employeee.cleaned_data['position'],
                                           employeee.cleaned_data['contact_info'],
                                           employeee.cleaned_data['specialities']
                                           )
            return redirect('workers')
    else:
        employeee = EmployeeForm()
    data={'employeee':employeee}
    return render(request,'vacancies_and_specialists/changing_employee.html',data)
def list_employers(request):
    employers=get_all_employers()
    # print(employers)
    return render(request,'vacancies_and_specialists/employers.html',{'employers':employers})
def changing_employer(request,slug_employer):
    if(request.method == "POST"):
        job=JobForm(request.POST)
        if(job.is_valid()):
            add_job_to_employer_by_slug(
                slug_employer,
                job.cleaned_data['job_title'],
                job.cleaned_data['job_description'],
                job.cleaned_data['job_location'],
                job.cleaned_data['job_salary'],
            )
            return redirect('list_employers')
    else:
        job=JobForm()
    data={'job':job}
    return render(request,'vacancies_and_specialists/job.html',data)
def list_specialities(request):
    c=get_specialities()
    return render(request,'vacancies_and_specialists/list_specialities.html',{'specialities':c})
# def delet_worker(request,slug_worker):
#     if
# request.method == 'POST':
#     worker.delete()
#     messages.success(request, f'Работник {worker.first_name} {worker.last_name} был успешно удалён!')
#     return redirect('workers')