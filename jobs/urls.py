from django.urls import path
from .views import jobs_view, recruiter_dashboard

urlpatterns = [

    path('', jobs_view),

    path(
        'recruiter-dashboard/',
        recruiter_dashboard,
        name='recruiter_dashboard'
    ),
]