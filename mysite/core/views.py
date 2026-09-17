from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.core.exceptions import PermissionDenied

from .forms import NoteForm
from .models import Note

def note_list(request):
    notes = Note.objects.all()
    return render(request, "core/note_list.html", {"notes": notes})


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "core/note_detail.html", {"note": note})


def note_recent(request):
    cutoff = timezone.now() - timedelta(hours=24)
    recent_notes = (
        Note.objects
        .filter(created_at__gte=cutoff)
        .order_by("-created_at")
    )
    return render(
        request,
        "core/note_recent.html",
        {"notes": recent_notes, "cutoff": cutoff},
    )

@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect("core:note_detail", pk=note.pk)
    else:
        form = NoteForm()

    return render(request, "core/note_form.html", {"form": form})

@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if note.author != request.user:
        raise PermissionDenied

    if request.method == "POST":
        form = NoteForm(request.POST, instance = note)
        if form.is_valid():
            note = form.save()
            return redirect("core:note_detail", pk=note.pk)
        else:
            form = NoteForm(instance=note)

    return render(request, "core/note_form.html", {"form": form})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if note.author != request.user:
        raise PermissionDenied

    if request.method == "POST":
        note.delete()
        return redirect("core:note_list")

    return render(request, "core/note_confirm_delete.html", {"note": note})
