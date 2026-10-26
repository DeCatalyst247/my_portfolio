from django.contrib import admin
from .models import Certification


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "issuing_organization",
        "issue_date",
        "expiry_date",
        "featured",
        "order",
    )

    list_filter = (
        "issuing_organization",
        "issue_date",
        "featured",
    )

    search_fields = (
        "name",
        "issuing_organization",
        "credential_id",
    )

    list_editable = ("featured", "order")

    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            "Certificate Information",
            {
                "fields": (
                    "name",
                    "issuing_organization",
                    "description",
                )
            },
        ),
        (
            "Credential Details",
            {
                "fields": (
                    "credential_id",
                    "credential_url",
                    "certificate_file",
                )
            },
        ),
        (
            "Validity",
            {
                "fields": (
                    "issue_date",
                    "expiry_date",
                    "does_not_expire",
                )
            },
        ),
        (
            "Display Settings",
            {
                "fields": ("featured", "order"),
            },
        ),
        (
            "System Information",
            {
                "fields": ("created_at", "updated_at"),
            },
        ),
    )