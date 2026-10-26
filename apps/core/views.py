from django.shortcuts import render

from .models import PortfolioProfile
from apps.projects.models import Project
from apps.experience.models import Experience
from apps.education.models import Education
from apps.skills.models import Skill
from apps.certifications.models import Certification
from apps.blog.models import Post
from django.utils import timezone


def home(request):
    profile = PortfolioProfile.objects.first()
    featured_projects = Project.objects.filter(featured=True)
    experiences = Experience.objects.all()[:3]
    educations = Education.objects.all()[:3]
    featured_skills = Skill.objects.filter(featured=True)
    featured_certifications = Certification.objects.filter(
    featured=True)
    latest_posts = Post.objects.filter(
    status="published",
    published_at__lte=timezone.now(),
)[:3]


    context = {
        "profile": profile,
        "featured_projects": featured_projects,
        "experiences": experiences,
        "educations": educations,
        "featured_skills" :featured_skills,
        "featured_certifications" :featured_certifications,
        "latest_posts":latest_posts,
    }

    return render(request, "home.html", context)