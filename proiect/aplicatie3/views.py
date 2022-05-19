from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie3.models import Studenti


class StudentiView(LoginRequiredMixin, ListView):
    model = Studenti
    template_name = 'aplicatie3/studenti_index.html'

# Create your views here.

class CreateStudentiView(LoginRequiredMixin, CreateView):
    model = Studenti
    fields = ['nume', 'prenume', 'specializare', 'grupa']
    template_name = "aplicatie3/studenti_form.html"

    def get_success_url(self):
        return reverse('studenti:lista_studenti')


class UpdateStudentiView(LoginRequiredMixin, UpdateView):
    model = Studenti
    fields = ['nume', 'prenume', 'specializare', 'grupa']
    template_name = "aplicatie3/studenti_form.html"

    def get_success_url(self):
        return reverse('studenti:lista_studenti')


@login_required
def delete_student(request, pk):
    Studenti.objects.filter(id=pk).update(activ=0)
    return redirect('studenti:lista_studenti')

@login_required
def activate_student(request, pk):
    Studenti.objects.filter(id=pk).update(activ=1)
    return redirect('studenti:lista_studenti')
