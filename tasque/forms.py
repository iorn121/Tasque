from django import forms
from .models import Task, TaskTag


class TaskForm(forms.ModelForm):
    class Meta:

        model = Task
        exclude = ('id', 'status', 'created_at', 'finished_at')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'class': 'form-control'}),
            # 'due_date': forms.NumberInput(attrs={'type': 'date'}),
            'due_date': forms.DateTimeInput(attrs={"type": "datetime-local"})
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = TaskTag
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
