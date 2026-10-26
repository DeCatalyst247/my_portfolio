from django.db import models


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)

    location = models.CharField(
        max_length=150,
        blank=True
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True,
        help_text="Leave empty if currently studying."
    )

    currently_studying = models.BooleanField(default=False)

    description = models.TextField(
        blank=True,
        help_text="Additional information about this education."
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
        return f"{self.degree} — {self.institution}"