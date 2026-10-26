from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    short_description = models.CharField(
        max_length=300,
        help_text="Short description used on project cards."
    )

    description = models.TextField(
        help_text="Full description of the project."
    )

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    technologies = models.CharField(
        max_length=500,
        help_text="Example: Django, Python, PostgreSQL, HTML, CSS"
    )

    github_url = models.URLField(
        blank=True
    )

    live_url = models.URLField(
        blank=True
    )

    featured = models.BooleanField(
        default=False,
        help_text="Display this project on the homepage."
    )

    completed_date = models.DateField(
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(
        default=0,
        help_text="Lower numbers appear first."
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["order", "-completed_date", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title