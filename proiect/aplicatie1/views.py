from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie1.models import Cursuri


class CursuriView(LoginRequiredMixin, ListView):
    model = Cursuri
    template_name = 'aplicatie1/cursuri_index.html'

# Create your views here.

class CreateCursuriView(LoginRequiredMixin, CreateView):
    model = Cursuri
    fields = ['NumeCurs', 'ProfCurs', 'DescriereCurs']
    template_name = "aplicatie1/cursuri_form.html"

    def get_success_url(self):
        return reverse('cursuri:lista_cursuri')


class UpdateCursuriView(LoginRequiredMixin, UpdateView):
    model = Cursuri
    fields = ['NumeCurs', 'ProfCurs', 'DescriereCurs']
    template_name = "aplicatie1/cursuri_form.html"

    def get_success_url(self):
        return reverse('cursuri:lista_cursuri')


@login_required
def delete_curs(request, pk):
    Cursuri.objects.filter(id=pk).update(activ=0)
    return redirect('cursuri:lista_cursuri')

@login_required
def activate_curs(request, pk):
    Cursuri.objects.filter(id=pk).update(activ=1)
    return redirect('cursuri:lista_cursuri')
