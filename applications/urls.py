from django.urls import path

from .views import (

    apply_job,

    recruiter_applications,

    shortlist_application,

    reject_application,
)


urlpatterns = [

    # APPLY JOB

    path(
        '<int:job_id>/',
        apply_job,
        name='apply_job'
    ),

    # RECRUITER APPLICATIONS

    path(
        'recruiter-applications/',
        recruiter_applications,
        name='recruiter_applications'
    ),

    # SHORTLIST APPLICATION

    path(
        'shortlist/<int:application_id>/',
        shortlist_application,
        name='shortlist_application'
    ),

    # REJECT APPLICATION

    path(
        'reject/<int:application_id>/',
        reject_application,
        name='reject_application'
    ),
]