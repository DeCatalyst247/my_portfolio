from django.shortcuts import render
from .models import Certification


def certification_list(request):
    certifications = Certification.objects.all()

    context = {
        "certifications": certifications,
    }

    return render(
        request,
        "certifications/certification_list.html",
        context,
    )