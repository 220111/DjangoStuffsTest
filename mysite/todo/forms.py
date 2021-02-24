from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.query import InstanceCheckMeta
from django.forms import widgets
from django.forms.widgets import TextInput
from django.forms.models import ModelForm, construct_instance

from .models import List, ListItem, SubListItem

class ListItemForm(ModelForm):
    class Meta:
        model = ListItem
        fields = ['item_text', 'done']
        widgets = {
            
        }
