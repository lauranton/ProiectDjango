from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie2.models import Profesori


class ProfesoriView(LoginRequiredMixin, ListView):
    model = Profesori
    template_name = 'aplicatie2/profesori_index.html'


class CreateProfesoriView(LoginRequiredMixin, CreateView):
    model = Profesori
    fields = ['nume', 'prenume', 'Profcurs']
    template_name = 'aplicatie2/profesori_form.html'

    def get_success_url(self):
        return reverse('profesori:lista_profesori')

class UpdateProfesoriView(LoginRequiredMixin, UpdateView):
    model = Profesori
    fields = ['nume', 'prenume', 'Profcurs']
    template_name = "aplicatie2/profesori_form.html"

    def get_success_url(self):
        return reverse('profesori:lista_profesori')

@login_required
def delete_profesor(request, pk):
    Profesori.objects.filter(id=pk).update(activ=0)
    return redirect('profesori:lista_profesori')

@login_required
def activate_profesor(request, pk):
    Profesori.objects.filter(id=pk).update(activ=1)
    return redirect('profesori:lista_profesori')

