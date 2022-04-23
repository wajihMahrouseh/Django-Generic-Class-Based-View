from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Make, Auto
# Create your views here.

# list view
class MakeList(ListView):
    model = Make


class AutoList(ListView):
    model = Auto
    # queryset = Auto.objects.all()
    allow_empty = True
    paginate_by = 12
    # ordering = 'nickname'
    template_name = 'gcbv/auto_list_v.html'
    context_object_name = 'autos'
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['zxc'] = 'Hello form get_context_data method!'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('nickname')