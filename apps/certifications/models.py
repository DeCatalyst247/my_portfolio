from django.db import models


class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)

    credential_id = models.CharField(
        max_length=200,
        blank=True,
    )

    credential_url = models.URLField(blank=True)

    issue_date = models.DateField()
    expiry_date = models.DateField(
        blank=True,
        null=True,
        help_text="Leave empty if the certificate does not expire.",
    )

    does_not_expire = models.BooleanField(default=False)

    certificate_file = models.FileField(
        upload_to="certificates/",
        blank=True,
        null=True,
    )

    description = models.TextField(blank=True)

    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-issue_date"]

    def __str__(self):
        return f"{self.name} — {self.issuing_organization}"