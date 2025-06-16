from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.views.generic.edit import FormView

from device.models import Device


class ProfileView(LoginRequiredMixin, View):
    template_name = "user/me.html"

    def get(self, request):
        context = {"user": request.user, "device_count": Device.objects.count()}
        return render(request, self.template_name, context)

    def post(self, request):
        user = request.user

        if "avatar" in request.FILES:
            self.handle_avatar_upload(request, user)
        else:
            self.update_user_info(request, user)

        return redirect("account_profile")

    def handle_avatar_upload(self, request, user):
        avatar = request.FILES["avatar"]

        if user.profile.avatar:
            user.profile.avatar.delete(save=False)

        filename = f"avatars/{user.id}"
        path = default_storage.save(filename, ContentFile(avatar.read()))
        user.profile.avatar = path
        user.profile.save()

        messages.success(request, "Votre photo de profil a été mise à jour.")

    def update_user_info(self, request, user):
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.save()

        messages.success(request, "Vos informations ont été mises à jour avec succès.")


class ChangePasswordView(LoginRequiredMixin, FormView):
    template_name = "app/profile.html"
    form_class = PasswordChangeForm

    def dispatch(self, request, *args, **kwargs):
        if request.method != "POST":
            return redirect("account_profile")
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        messages.success(self.request, "Votre mot de passe a été changé avec succès.")
        return redirect("account_profile")

    def form_invalid(self, form):
        messages.error(self.request, "Veuillez corriger les erreurs ci-dessous.")
        return super().form_invalid(form)
