from django.shortcuts import render, redirect

from notes_app.common.profile_utils import get_profile
from notes_app.notes.forms import ProfileForm, AddNoteForm, EditNoteForm, DeleteNoteForm
from notes_app.notes.models import Note


def home_page(request):
    profile = get_profile()
    if profile:
        notes = Note.objects.all()
        context = {
            'notes': notes,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        return redirect('create profile')


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def show_profile_page(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    profile.delete()
    Note.objects.all().delete()
    return redirect('home page')


def add_note(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = AddNoteForm()
    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditNoteForm(instance=note)
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('home page')
    else:
        form = DeleteNoteForm(instance=note)
        context = {
            'form': form,
            'note': note,
        }
        return render(request, 'note-delete.html', context)


def show_note_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)














