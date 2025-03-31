from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from app.models import Device

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('app:dashboard')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'app/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
            return redirect('app:register')
            
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur existe déjà.')
            return redirect('app:register')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Cet email est déjà utilisé.')
            return redirect('app:register')
            
        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('app:dashboard')
        
    return render(request, 'app/register.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('app:login')

@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        messages.success(request, 'Vos informations ont été mises à jour avec succès.')
        return redirect('app:profile')
    
    context = {
        'user': request.user,
        'device_count': Device.objects.count()
    }
    return render(request, 'app/profile.html', context)

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Votre mot de passe a été modifié avec succès.')
            return redirect('app:profile')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'app/profile.html', {'password_form': form}) 