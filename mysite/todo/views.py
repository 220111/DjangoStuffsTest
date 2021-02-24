from django.http import HttpResponseRedirect, request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from .models import List, ListItem, SubListItem
from .forms import ListItemForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'latest_todo_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return List.objects.order_by('-pub_date')[:5]

def detail(request, list_id):
    list = get_object_or_404(List, pk=list_id)
    if request.method == 'POST':
        form = ListItemForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('detail')
    else:
        form = ListItemForm()
    return render(request,
                  'todo/detail.html',
                  {
                      'form': form, 
                      'list': list
                  })

    