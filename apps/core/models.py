from django.db import models


class PortfolioProfile(models.Model):
    name = models.CharField(max_length=150)
    professional_title = models.CharField(max_length=200)

    short_bio = models.TextField(
        help_text="Short introduction displayed on the homepage."
    )

    about = models.TextField(
        help_text="Detailed biography displayed on the About section."
    )

    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=150, blank=True)

    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)

    cv = models.FileField(
        upload_to="documents/",
        blank=True,
        null=True
    )

    hero_heading = models.CharField(
        max_length=200,
        default="Building Solutions Through Technology"
    )

    hero_description = models.TextField(
        blank=True
    )

    available_for_work = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    def __str__(self):
        return self.name