from django.db import connection
from django.db.models.expressions import result


def add_employer(emp_name, emp_location, emp_contact_info,job_title,job_description,job_location,job_salary):
    with connection.cursor() as cursor:
        cursor.execute("CALL create_employer_and_job(%s, %s, %s, %s, %s, %s, %s);", [
            emp_name ,emp_location, emp_contact_info,
            job_title,job_description,job_location,job_salary])


def get_jobs_and_employers():
    with connection.cursor() as cursor:
        cursor.callproc('jobs_and_employers')
        jobs_and_employers = cursor.fetchall()
    # print(jobs_and_employers[0])
    return jobs_and_employers
def search_jobs_by_title(search_query):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM search_jobs_by_title(%s);', [search_query])
        result = cursor.fetchall()
    return result
def get_jobs():
    with connection.cursor() as cursor:
        cursor.callproc('get_jobs')
        result = cursor.fetchall()
    return result
def search_job_by_slug_with_employer(p_slug):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM search_job_by_slug_with_employer(%s);", [p_slug])
        result=cursor.fetchall()
    return result
def assign_jobs_to_worker(worker_first_name,worker_last_name ,worker_position ,worker_contact_info ,job_ids):
    job_ids_str = '{' + ','.join(map(str, job_ids)) + '}'
    with connection.cursor() as cursor:
        cursor.execute("""
                    SELECT assign_jobs_to_worker(%s, %s, %s, %s, %s);
                """, [worker_first_name, worker_last_name, worker_position, worker_contact_info, job_ids_str])
def get_workers():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM workers();")
        result = cursor.fetchall()
    return result
def get_all_specialities():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM get_all_specialities();")
        result = cursor.fetchall()
        print(result)
    return [(speciality[0], speciality[1]) for speciality in result]
def get_worker_details_by_slug(worker_slug):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM get_worker_details_by_slug(%s);", [worker_slug])
        result = cursor.fetchall()
    return result
def delete_worker_by_slug(worker_slug):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM  delete_worker_by_slug(%s);", [worker_slug])
def  update_worker_and_specialities(worker_slug,new_first_name,new_last_name,new_position,new_contact_info,new_job_ids):
    job_ids_str = '{' + ','.join(map(str, new_job_ids)) + '}'
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM update_worker_and_specialities(%s, %s, %s, %s, %s, %s);", [worker_slug,new_first_name,new_last_name,new_position,new_contact_info,job_ids_str])
def get_all_employers():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM get_all_employers();")
        result = cursor.fetchall()
    return result
def get_employer_and_jobs_by_slug(employer_slug_param):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM get_employer_and_jobs_by_slug(%s)",[employer_slug_param])
        result = cursor.fetchall()
    return result
def delete_employer_and_jobs_by_slug(employer_slug):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM delete_employer_and_jobs_by_slug(%s)",[employer_slug])
def add_job_to_employer_by_slug(
    employer_slug,
    new_job_title,
    job_description,
     job_location,
     job_salary):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM add_job_to_employer_by_slug(%s, %s, %s, %s, %s);", [employer_slug,
    new_job_title,
    job_description,
     job_location,
     job_salary])
def delete_job_by_slug(job_slug_param ):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM delete_job_by_slug(%s);", [job_slug_param])

def get_specialities():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM get_specialities();")
        result = cursor.fetchall()
    return result

# def authenticate_or_register(cursor, name, password, location=None, contact_info=None):
#     with connection.cursor() as cursor:
#         cursor.callproc(
#             'authenticate_or_register_employer',
#             [None, None, name, password, location, contact_info]
#         )
#         result = cursor.fetchone()
#     if result:
#         employer_name, slug = result
#
#         return {
#             'employer_name': employer_name,
#             'slug':slug
#         }
#     return None


