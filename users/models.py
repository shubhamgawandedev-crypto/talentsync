from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    # =====================================
    # ROLE
    # =====================================

    ROLE_CHOICES = (

        ('admin', 'Admin'),

        ('recruiter', 'Recruiter'),

        ('candidate', 'Candidate'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='candidate'
    )


    # =====================================
    # COMMON FIELDS
    # =====================================

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    profile_pic = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True
    )

    bio = models.TextField(
        blank=True,
        null=True
    )

    linkedin = models.URLField(
        blank=True,
        null=True
    )

    is_verified = models.BooleanField(
        default=False
    )


    # =====================================
    # CANDIDATE FIELDS
    # =====================================

    headline = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    skills = models.TextField(
        blank=True,
        null=True
    )

    education = models.TextField(
        blank=True,
        null=True
    )

    experience = models.TextField(
        blank=True,
        null=True
    )

    github = models.URLField(
        blank=True,
        null=True
    )

    resume = models.FileField(
        upload_to='candidate_resumes/',
        blank=True,
        null=True
    )


    # =====================================
    # RECRUITER FIELDS
    # =====================================

    company_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    designation = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    company_website = models.URLField(
        blank=True,
        null=True
    )

    industry = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    company_description = models.TextField(
        blank=True,
        null=True
    )


    # =====================================
    # STRING
    # =====================================

    def __str__(self):

        return self.username