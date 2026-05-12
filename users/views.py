from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from django.contrib.auth.decorators import login_required


from django.contrib import messages

from django.conf import settings


from .models import User


# =========================
# REGISTER
# =========================

def register_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        email = request.POST.get('email')

        password = request.POST.get('password')

        role = request.POST.get('role')

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                'Username already exists'
            )

            return redirect('/register/')

        if User.objects.filter(email=email).exists():

            messages.error(
                request,
                'Email already exists'
            )

            return redirect('/register/')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role,
            is_active=True,
            is_verified=True
        )

        messages.success(
            request,
            'Registration successful. You can now log in.'
        )

        return redirect('/login/')

    return render(request, 'register.html')


# =========================
# VERIFY EMAIL
# =========================

def verify_email(request, user_id):

    try:

        user = User.objects.get(id=user_id)

        user.is_active = True

        user.is_verified = True

        user.save()

        messages.success(
            request,
            'Email verified successfully.'
        )

        return redirect('/login/')

    except User.DoesNotExist:

        messages.error(
            request,
            'Invalid verification link.'
        )

        return redirect('/register/')


# =========================
# LOGIN
# =========================

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user:

            if not user.is_verified:

                messages.error(
                    request,
                    'Please verify your email first.'
                )

                return redirect('/login/')

            login(request, user)

            if user.role == 'recruiter':

                return redirect(
                    '/jobs/recruiter-dashboard/'
                )

            return redirect('/candidate-dashboard/')

        else:

            messages.error(
                request,
                'Invalid username or password'
            )

    return render(request, 'login.html')


# =========================
# LOGOUT
# =========================

def logout_view(request):

    logout(request)

    return redirect('/login/')


# =========================
# PROFILE
# =========================

@login_required
def profile_view(request):

    user = request.user

    if request.method == 'POST':

        # COMMON FIELDS

        user.first_name = request.POST.get(
            'first_name',
            ''
        )

        user.last_name = request.POST.get(
            'last_name',
            ''
        )

        user.phone = request.POST.get(
            'phone',
            ''
        )

        user.bio = request.POST.get(
            'bio',
            ''
        )

        user.linkedin = request.POST.get(
            'linkedin',
            ''
        )

        # =====================================
        # CANDIDATE PROFILE
        # =====================================

        if user.role == 'candidate':

            user.headline = request.POST.get(
                'headline',
                ''
            )

            user.skills = request.POST.get(
                'skills',
                ''
            )

            user.education = request.POST.get(
                'education',
                ''
            )

            user.experience = request.POST.get(
                'experience',
                ''
            )

            user.github = request.POST.get(
                'github',
                ''
            )

            if request.FILES.get('resume'):

                user.resume = request.FILES.get(
                    'resume'
                )

        # =====================================
        # RECRUITER PROFILE
        # =====================================

        elif user.role == 'recruiter':

            user.company_name = request.POST.get(
                'company_name',
                ''
            )

            user.designation = request.POST.get(
                'designation',
                ''
            )

            user.company_website = request.POST.get(
                'company_website',
                ''
            )

            user.industry = request.POST.get(
                'industry',
                ''
            )

            user.company_description = request.POST.get(
                'company_description',
                ''
            )

        # =====================================
        # PROFILE IMAGE
        # =====================================

        if request.FILES.get('profile_pic'):

            user.profile_pic = request.FILES.get(
                'profile_pic'
            )

        user.save()

        messages.success(
            request,
            'Profile updated successfully.'
        )

        return redirect('/profile/')

    # =====================================
    # RECRUITER PROFILE PAGE
    # =====================================

    if user.role == 'recruiter':

        return render(
            request,
            'recruiter_profile.html',
            {
                'user_data': user
            }
        )

    # =====================================
    # CANDIDATE PROFILE PAGE
    # =====================================

    return render(
        request,
        'profile.html',
        {
            'user_data': user
        }
    )