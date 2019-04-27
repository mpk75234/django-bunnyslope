from django.shortcuts import render
from .models import Job


def landing(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/landing.html', {'jobs': jobs})