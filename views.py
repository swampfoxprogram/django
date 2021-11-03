from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "google.html")  # render css,javascript,image,video,audio
