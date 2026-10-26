from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True,
    )

    excerpt = models.CharField(
        max_length=300,
        help_text="A short summary displayed on article cards.",
    )

    content = models.TextField()

    cover_image = models.ImageField(
        upload_to="blog/",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft",
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title