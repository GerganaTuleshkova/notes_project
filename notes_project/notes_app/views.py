from django.shortcuts import render, redirect

from notes_project.notes_app.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from notes_project.notes_app.helpers_functions import get_profile
from notes_project.notes_app.models import Note


def home(request):
    profile = get_profile()
    if not profile:
        return create_profile(request)
    notes = Note.objects.all()
    context = {
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        # create form with POST
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        # create empty form
        form = CreateNoteForm()

    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        # create form with POST
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
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
        # create form with POST
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)


def profile_details(request):
    profile = get_profile()
    notes = Note.objects.all()
    notes_count = len(notes)
    context = {
        'profile': profile,
        'notes_count': notes_count,
    }

    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        # create form with POST
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        # create empty form
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def delete_profile(request, pk):
    profile = get_profile()
    notes = Note.objects.all()
    notes.delete()
    profile.delete()
    return redirect('home')
