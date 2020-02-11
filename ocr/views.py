from django.shortcuts import render
from django.views.generic import FormView

from . import forms
from .common.networking.ocr_space import ocr

class UploadDocumentView(FormView):
    template_name = 'index.html'
    form_class = forms.DocumentForm

    def form_valid(self, form):
        context = self.get_context_data()
        f = self.request.FILES['file']
        context['results'] = ocr(f.name, f.read())
        return render(self.request, self.template_name, context)
