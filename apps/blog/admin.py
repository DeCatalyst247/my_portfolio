from django.contrib import admin
from django.utils import timezone
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "published_at",
        "updated_at",
    )

    list_filter = (
        "status",
        "published_at",
    )

    search_fields = (
        "title",
        "excerpt",
        "content",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Article Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "excerpt",
                    "cover_image",
                )
            },
        ),
        (
            "Article Content",
            {
                "fields": ("content",),
            },
        ),
        (
            "Publication",
            {
                "fields": (
                    "status",
                    "published_at",
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

    def save_model(self, request, obj, form, change):
        if obj.status == "published" and not obj.published_at:
            obj.published_at = timezone.now()

        super().save_model(request, obj, form, change)