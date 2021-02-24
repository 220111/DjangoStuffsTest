from django.utils.safestring import mark_safe
from django.urls import reverse

from django.contrib import admin

from .models import List, ListItem, SubListItem

class EditLinkToInlineObject(object):
    def edit_link(self, instance):
        url = reverse('admin:%s_%s_change' % (
            instance._meta.app_label,  instance._meta.model_name),  args=[instance.pk] )
        if instance.pk:
            return mark_safe(u'<a href="{u}">edit</a>'.format(u=url))
        else:
            return ''

class SubItemInLine(admin.TabularInline):
    model = SubListItem
    extra = 0

class ItemInLine(EditLinkToInlineObject, admin.TabularInline):
    model = ListItem
    extra = 0
    readonly_fields = ('edit_link', )
    

class ListItemAdmin(admin.ModelAdmin):
    inlines = [SubItemInLine]
    

class ListAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['list_name']}),
        ('Date Information',{'fields': ['pub_date'], 'classes':['colapes']}),
    ]
    inlines = [ItemInLine]

admin.site.register(ListItem, ListItemAdmin)
admin.site.register(List, ListAdmin)
