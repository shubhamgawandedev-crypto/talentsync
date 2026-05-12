from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Application

from jobs.models import Job



# =========================================
# APPLY JOB
# =========================================
@login_required(login_url='/login/')
def apply_job(request, job_id):

    job = Job.objects.get(id=job_id)

    # Prevent duplicate applications
    already_applied = Application.objects.filter(
        candidate=request.user,
        job=job
    ).exists()

    if already_applied:

        messages.warning(
            request,
            'You already applied for this job.'
        )

        return redirect('/candidate-dashboard/')

    if request.method == 'POST':

        resume = request.FILES.get('resume')

        cover_letter = request.POST.get(
            'cover_letter'
        )

        Application.objects.create(

            candidate=request.user,

            job=job,

            resume=resume,

            cover_letter=cover_letter,
        )

        messages.success(
            request,
            'Application submitted successfully!'
        )

        return redirect('/candidate-dashboard/')

    return render(
        request,
        'apply.html',
        {
            'job': job
        }
    )

# =========================================
# RECRUITER APPLICATIONS
# =========================================

@login_required
def recruiter_applications(request):

    # SECURITY

    if request.user.role != 'recruiter':

        return redirect('/')

    # ONLY RECRUITER JOB APPLICATIONS

    applications = Application.objects.filter(
        job__recruiter=request.user
    ).select_related(
        'candidate',
        'job'
    ).order_by('-applied_at')

    context = {

        'applications': applications
    }

    return render(
        request,
        'recruiter_applications.html',
        context
    )


# =========================================
# SHORTLIST APPLICATION
# =========================================

@login_required
def shortlist_application(request, application_id):
    # GET APPLICATION

    application = get_object_or_404(
        Application,
        id=application_id
    )

    # SECURITY CHECK

    if request.user != application.job.recruiter:
        return redirect('/')

    # UPDATE STATUS

    application.status = 'shortlisted'

    application.save()

    return redirect(
        '/jobs/recruiter-dashboard/'
    )


# =========================================
# REJECT APPLICATION
# =========================================

@login_required
def reject_application(request, application_id):
    # GET APPLICATION

    application = get_object_or_404(
        Application,
        id=application_id
    )

    # SECURITY CHECK

    if request.user != application.job.recruiter:
        return redirect('/')

    # UPDATE STATUS

    application.status = 'rejected'

    application.save()

    return redirect(
        '/jobs/recruiter-dashboard/'
    )