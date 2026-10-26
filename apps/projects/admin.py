from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "featured",
        "completed_date",
        "order",
        "updated_at",
    )

    list_filter = (
        "featured",
        "completed_date",
    )

    search_fields = (
        "title",
        "short_description",
        "description",
        "technologies",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_editable = (
        "featured",
        "order",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Project Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "short_description",
                    "description",
                    "image",
                )
            },
        ),

        (
            "Technologies",
            {
                "fields": (
                    "technologies",
                )
            },
        ),

        (
            "Project Links",
            {
                "fields": (
                    "github_url",
                    "live_url",
                )
            },
        ),

        (
            "Display Settings",
            {
                "fields": (
                    "featured",
                    "order",
                    "completed_date",
                )
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