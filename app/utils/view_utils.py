from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template.loader import render_to_string


class AddView(FormView):
    formset_class = None

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        formset = self.get_formset()
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.formset_class:
            context["formset"] = self.get_formset()
        return context

    def get_formset(self, data=None):
        """Instancie le formset si formset_class est défini."""
        if self.formset_class:
            return self.formset_class(data)
        return None

    def form_valid(self, form):
        modele = form.save()
        formset = self.get_formset(self.request.POST)

        if formset and formset.is_valid():
            # Traiter les données du formset
            for subform in formset:
                if subform.cleaned_data:
                    print("Formset Data:", subform.cleaned_data)

        html = render_to_string(
            "app/components/formResponse.html",
            {
                "success": True,
                "modele": modele,
            },
        )

        return HttpResponse(html, status=200)

    def form_invalid(self, form):
        formset = self.get_formset(self.request.POST)
        html = render_to_string(
            "app/components/formResponse.html",
            {
                "success": False,
                "form": form,
                "formset": formset,
            },
        )

        return HttpResponse(html, status=200)
