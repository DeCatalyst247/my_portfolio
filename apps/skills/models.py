from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator



class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("programming", "Programming Languages"),
        ("backend", "Backend Development"),
        ("frontend", "Frontend Development"),
        ("database", "Databases"),
        ("tools", "Tools & Technologies"),
        ("engineering", "Hardware & Engineering"),
        ("other", "Other Skills"),
    ]

    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
    )

    proficiency = models.PositiveSmallIntegerField(
       default=50,
       validators=[
           MinValueValidator(0),
           MaxValueValidator(100),
        ],
       help_text="Enter a value from 0 to 100.",
    )

    years_of_experience = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0,
    )

    description = models.CharField(
        max_length=250,
        blank=True,
    )

    featured = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["category", "order", "name"]

    def __str__(self):
        return self.name