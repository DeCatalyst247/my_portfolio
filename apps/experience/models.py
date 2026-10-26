from django.db import models


class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    location = models.CharField(max_length=150, blank=True)

    employment_type = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: Internship, IT Placement, Freelance, Full-time"
    )

    description = models.TextField()

    start_date = models.DateField()
    end_date = models.DateField(
        blank=True,
        null=True,
        help_text="Leave empty if this experience is ongoing."
    )

    currently_working = models.BooleanField(default=False)

    technologies = models.CharField(
        max_length=500,
        blank=True,
        help_text="Example: Django, Python, HTML, CSS"
    )

    order = models.PositiveIntegerField(
        default=0,
        help_text="Lower numbers appear first."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-start_date"]

    def __str__(self):
        return f"{self.job_title} — {self.organization}"