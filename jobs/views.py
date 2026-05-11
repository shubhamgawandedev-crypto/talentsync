from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import Job

from applications.models import Application


# =========================================
# JOB LIST VIEW
# =========================================

def jobs_view(request):

    jobs = Job.objects.all().order_by('-created_at')

    search = request.GET.get('search')

    if search:

        jobs = jobs.filter(
            title__icontains=search
        )

    context = {

        'jobs': jobs
    }

    return render(
        request,
        'jobs.html',
        context
    )


# =========================================
# RECRUITER DASHBOARD
# =========================================

@login_required
def recruiter_dashboard(request):

    # SECURITY CHECK

    if request.user.role != 'recruiter':

        return redirect('/')

    # CREATE JOB

    if request.method == 'POST':

        Job.objects.create(

            recruiter=request.user,

            title=request.POST.get('title'),

            company=request.POST.get('company'),

            location=request.POST.get('location'),

            salary=request.POST.get('salary'),

            skills=request.POST.get('skills'),

            description=request.POST.get('description')
        )

        return redirect(
            '/jobs/recruiter-dashboard/'
        )

    # RECRUITER JOBS

    jobs = Job.objects.filter(
        recruiter=request.user
    ).order_by('-created_at')

    # APPLICATIONS OF RECRUITER JOBS

    applications = Application.objects.filter(
        job__recruiter=request.user
    ).select_related(
        'candidate',
        'job'
    ).order_by('-applied_at')

    # STATS

    total_jobs = jobs.count()

    total_applications = applications.count()

    active_jobs = jobs.count()

    shortlisted = applications.filter(
        status='shortlisted'
    ).count()

    rejected = applications.filter(
        status='rejected'
    ).count()

    pending = applications.filter(
        status='applied'
    ).count()

    # CONTEXT

    context = {

        'jobs': jobs,

        'applications': applications,

        'total_jobs': total_jobs,

        'total_applications': total_applications,

        'active_jobs': active_jobs,

        'shortlisted': shortlisted,

        'rejected': rejected,

        'pending': pending,
    }

    return render(
        request,
        'recruiter_dashboard.html',
        context
    )