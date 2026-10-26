from django.contrib import admin
from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "job_title",
        "organization",
        "employment_type",
        "start_date",
        "end_date",
        "currently_working",
        "order",
    )

    list_filter = (
        "currently_working",
        "employment_type",
    )

    search_fields = (
        "job_title",
        "organization",
        "description",
        "technologies",
    )

    list_editable = (
        "currently_working",
        "order",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Experience Information",
            {
                "fields": (
                    "job_title",
                    "organization",
                    "location",
                    "employment_type",
                )
            },
        ),
        (
            "Description",
            {
                "fields": (
                    "description",
                    "technologies",
                )
            },
        ),
        (
            "Duration",
            {
                "fields": (
                    "start_date",
                    "end_date",
                    "currently_working",
                )
            },
        ),
        (
            "Display Settings",
            {
                "fields": ("order",),
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
