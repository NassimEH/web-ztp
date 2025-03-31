from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'app/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Erreur lors de l\'inscription. Veuillez corriger les erreurs ci-dessous.')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('auth:login')

class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'app/profile.html'
    fields = ['username', 'email', 'first_name', 'last_name']
    success_url = reverse_lazy('auth:profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Profil mis à jour avec succès!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Erreur lors de la mise à jour du profil.')
        return super().form_invalid(form) 