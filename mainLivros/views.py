from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Livro


class LivroList(ListView):
    model = Livro


class LivroDetail(DetailView):
    model = Livro


class LivroCreate(CreateView):
    model = Livro
    fields = '__all__'
    success_url = reverse_lazy('mainLivros:list')


class LivroUpdate(UpdateView):
    model = Livro
    fields = '__all__'
    success_url = reverse_lazy('mainLivros:list')


class LivroDelete(DeleteView):
    model = Livro
    fields = '__all__'
    success_url = reverse_lazy('mainLivros:list')
