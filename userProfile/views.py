from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import UserUpdateForm, ProfileForm

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user) # либо получаем профиль, либо создаем, get_or_create(user=request.user) вернет если есть пользователь с текущем профилем
    context = {
        'profile': profile,
        'page_title': f'Профиль {request.user.username}'
    }
    return render(request, 'userProfile/profile.html', context)

@login_required
def profile_edit(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Профиль обновлен')
            return redirect('userProfile:profile')
        else:
            messages.error(request, 'Ошибки в форме')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'page_title': 'Редактирование профиля'
    }
    return render(request, 'userProfile/profile_edit.html', context)