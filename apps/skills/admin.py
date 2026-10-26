from django.contrib import admin
from .models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "proficiency",
        "featured",
        "order",
        "updated_at",
    )

    list_filter = (
        "category",
        "featured",
    )

    search_fields = (
        "name",
        "description",
    )

    list_editable = (
        "proficiency",
        "featured",
        "order",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Skill Information",
            {
                "fields": (
                    "name",
                    "category",
                    "description",
                )
            },
        ),
        (
            "Proficiency",
            {
                "fields": (
                    "proficiency",
                    "years_of_experience",
                )
            },
        ),
        (
            "Display Settings",
            {
                "fields": (
                    "featured",
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