from django import forms

from notes_app.notes.models import Profile, Note


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class AddNoteForm(NoteForm):
    pass


class EditNoteForm(NoteForm):
    pass


class DeleteNoteForm(NoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'

