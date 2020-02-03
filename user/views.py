from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        registration = UserCreationForm(request.POST)
        if registration.is_valid():
            registration.save()
            username = registration.cleaned_data.get('username')
            password = registration.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(
                request, f'Your account, {username} has been successfully created, You may now create a post or update your profile.')
            return redirect('user-profile-update')
    context = {
        'title': 'Register',
        'form': UserCreationForm()
    }
    return render(request, 'register.html', context)


@login_required
def profile_user(request, pk):
    user_profile = get_object_or_404(Profile, pk=pk)
    context = {
        'title': 'Profile page',
        'obj': user_profile
    }
    return render(request, 'profile.html', context)


@login_required
def profile_update(request):
    user_form = UserUpdateForm(
        request.POST or None, request.FILES or None, instance=request.user)
    profile_form = ProfileUpdateForm(
        request.POST or None, request.FILES or None, instance=request.user.profile)
    if request.method == "POST":
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'You profile is successfully updated!')
            return redirect('/')
    context = {
        'title': 'Update Profile',
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'update_profile.html', context)
