from django.shortcuts import render


def landing(request):
    return render(request, 'blog/landing.html', {'msg': 'I need to get laid'})