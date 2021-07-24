from django.contrib import admin

from notes_app.notes.models import Profile, Note

admin.site.register(Profile)
admin.site.register(Note)
