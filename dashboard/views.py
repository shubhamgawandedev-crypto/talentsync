from django.shortcuts import render
from applications.models import Application


def candidate_dashboard(request):

    applications = Application.objects.filter(
        candidate=request.user
    )

    total_applications = applications.count()

    shortlisted = applications.filter(
        status='shortlisted'
    ).count()

    rejected = applications.filter(
        status='rejected'
    ).count()

    context = {
        'applications': applications,
        'total_applications': total_applications,
        'shortlisted': shortlisted,
        'rejected': rejected,
    }

    return render(
        request,
        'candidate_dashboard.html',
        context
    )