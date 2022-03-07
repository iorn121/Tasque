from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:

        model = Task
        exclude = ('id', 'status', 'created_at', 'finished_at')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'class': 'form-control'}),
            'due_date': forms.NumberInput(attrs={'type': 'date'}),
        }
