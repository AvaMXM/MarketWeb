from django.shortcuts import render, get_object_or_404
from .models import User


def index(request):
    return render(request, 'index.html')


def profile(request):
    profile_user = get_object_or_404(User, username=request.user)
    return render(request, 'profile.html', {'user': profile_user})
