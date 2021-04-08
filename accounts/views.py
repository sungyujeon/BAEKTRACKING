from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_GET, require_safe
from .forms import CustomUserCreationForm, CustomUserChangeForm


User = get_user_model()

@require_http_methods(['GET', 'POST'])
def signup(request):
    # if request.user.is_authenticated:
    #     return redirect('home')  # 경로 수정 필요

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # 경로 수정 필요
    else:
        form = CustomUserCreationForm()
        
    context = {
        'form': form,
    }

    return render(request, 'accounts/form.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    # if request.user.is_authenticated:
    #     return redirect('home')  # 경로 수정 필요
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'home')  # 경로 수정 필요
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'accounts/form.html', context)  # 경로 수정 필요


@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')  # 경로 수정 필요


@require_POST
def delete(request):
    # if request.user.is_authenticated:
    #     request.user.delete()
    
    return redirect('home')  # 경로 수정 필요


@require_http_methods(['GET', 'POST'])
@login_required
def update(request, *args, **kwargs):
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', user.pk)
        
    else:
        form = CustomUserChangeForm(instance=user)
    
    context = {
        'form': form,
    }

    return render(request, 'accounts/update.html', context)

        
def profile(request, *args, **kwargs):
    user_info = get_object_or_404(get_user_model(), pk=kwargs.get('pk'))
    context = {
        'user_info': user_info,
    }
    return render(request, 'accounts/profile.html', context)



def pw_update(request, *args, **kwargs):

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('accounts:profile', request.user.pk)

    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)
