# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from notes.models import Note

class NoteAdmin(admin.ModelAdmin):
  list_display = ( 'id', 'title', 'note',)
  search_fields = ('title', 'note',)
  
admin.site.register(Note, NoteAdmin)