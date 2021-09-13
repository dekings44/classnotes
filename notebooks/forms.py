from django import forms
from .models import Notes


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['note_topic', 'category', 'note_body']
        widgets = {
            'note_topic' : forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(attrs={'class': 'form-control'}),
            'note_body' : forms.Textarea(attrs={'class': 'form-control'}),
        }