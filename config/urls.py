from django.contrib import admin

from django.urls import path, include

from django.shortcuts import render

from django.conf import settings

from django.conf.urls.static import static


# =========================
# HOME VIEW
# =========================

def home(request):

    return render(
        request,
        'home.html'
    )


# =========================
# URL PATTERNS
# =========================

urlpatterns = [

    # ADMIN

    path(
        'admin/',
        admin.site.urls
    ),

    # HOME

    path(
        '',
        home,
        name='home'
    ),

    # USERS

    path(
        '',
        include('users.urls')
    ),

    # JOBS

    path(
        'jobs/',
        include('jobs.urls')
    ),

    # APPLICATIONS

    path(
        'applications/',
        include('applications.urls')
    ),

    # DASHBOARD

    path(
        'candidate-dashboard/',
        include('dashboard.urls')
    ),

    # DJANGO ALLAUTH

    path(
        'accounts/',
        include('allauth.urls')
    ),

]


# =========================
# MEDIA FILES
# =========================

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)