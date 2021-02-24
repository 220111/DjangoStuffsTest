from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import CollectedItem

class IndexView(generic.ListView):
    template_name = 'data/index.html'
    context_object_name = 'latest_item_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return CollectedItem.objects.order_by('-collect_date')

class DetailView(generic.DetailView):
    model = CollectedItem
    template_name = 'data/detail.html'
