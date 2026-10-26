from django.contrib import admin
from .models import PortfolioProfile


@admin.register(PortfolioProfile)
class PortfolioProfileAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "professional_title",
        "email",
        "available_for_work",
        "updated_at",
    )

    readonly_fields = (
        "updated_at",
    )

    fieldsets = (
        (
            "Personal Information",
            {
                "fields": (
                    "name",
                    "professional_title",
                    "profile_image",
                    "short_bio",
                    "about",
                )
            },
        ),
        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone",
                    "location",
                )
            },
        ),
        (
            "Social Links",
            {
                "fields": (
                    "github_url",
                    "linkedin_url",
                    "twitter_url",
                )
            },
        ),
        (
            "Hero Section",
            {
                "fields": (
                    "hero_heading",
                    "hero_description",
                    "available_for_work",
                )
            },
        ),
        (
            "Documents",
            {
                "fields": (
                    "cv",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "updated_at",
                )
            },
        ),
    )

    def has_add_permission(self, request):
        return not PortfolioProfile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False