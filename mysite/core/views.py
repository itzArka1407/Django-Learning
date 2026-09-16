from datetime import timedelta

from django.shortcuts import get_object_or_404, render
from django.utils import timezone

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
