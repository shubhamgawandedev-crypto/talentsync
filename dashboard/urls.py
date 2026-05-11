from django.urls import path
from .views import candidate_dashboard

urlpatterns = [

    path(
        '',
        candidate_dashboard,
        name='candidate_dashboard'
    ),

]