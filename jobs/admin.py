from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'company',
        'location',
        'salary',
        'recruiter',
        'created_at',
    )

    list_filter = (
        'location',
        'company',
        'created_at',
    )

    search_fields = (
        'title',
        'company',
        'skills',
    )

    ordering = ('-created_at',)

    readonly_fields = (
        'created_at',
    )

    list_per_page = 10

    fieldsets = (

        ('Job Information', {
            'fields': (
                'title',
                'company',
                'location',
                'salary',
            )
        }),

        ('Requirements', {
            'fields': (
                'skills',
                'description',
            )
        }),

        ('Recruiter Details', {
            'fields': (
                'recruiter',
            )
        }),

        ('Date Information', {
            'fields': (
                'created_at',
            )
        }),
    )