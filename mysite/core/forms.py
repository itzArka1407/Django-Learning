from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "body", "author"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Note title"}),
            "body": forms.Textarea(attrs={"rows": 6, "placeholder": "Write something..."}),
        }
