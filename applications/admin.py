from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'candidate',
        'job',
        'status',
        'applied_at',
    )

    list_filter = (
        'status',
        'applied_at',
    )

    search_fields = (
        'candidate__username',
        'job__title',
    )

    ordering = ('-applied_at',)

    readonly_fields = (
        'applied_at',
    )

    list_editable = (
        'status',
    )

    list_per_page = 10

    fieldsets = (

        ('Candidate Information', {
            'fields': (
                'candidate',
                'job',
            )
        }),

        ('Resume Details', {
            'fields': (
                'resume',
                'cover_letter',
            )
        }),

        ('Application Status', {
            'fields': (
                'status',
            )
        }),

        ('Date Information', {
            'fields': (
                'applied_at',
            )
        }),
    )