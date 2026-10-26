from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "institution",
        "degree",
        "field_of_study",
        "start_date",
        "end_date",
        "currently_studying",
        "order",
    )

    list_filter = (
        "currently_studying",
        "institution",
    )

    search_fields = (
        "institution",
        "degree",
        "field_of_study",
        "description",
    )

    list_editable = (
        "currently_studying",
        "order",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Education Information",
            {
                "fields": (
                    "institution",
                    "degree",
                    "field_of_study",
                    "location",
                )
            },
        ),
        (
            "Duration",
            {
                "fields": (
                    "start_date",
                    "end_date",
                    "currently_studying",
                )
            },
        ),
        (
            "Additional Information",
            {
                "fields": (
                    "description",
                )
            },
        ),
        (
            "Display Settings",
            {
                "fields": (
                    "order",
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