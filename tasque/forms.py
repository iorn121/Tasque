from django import forms
from .models import Task, TaskTag
from django.db.models import Q


class TaskForm(forms.ModelForm):
    class Meta:

        model = Task
        exclude = ('id', 'status', 'user', 'created_at', 'finished_at')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'class': 'form-control'}),
            # 'due_date': forms.NumberInput(attrs={'type': 'date'}),
            'due_date': forms.DateTimeInput(attrs={"type": "datetime-local"})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['tag'].queryset = TaskTag.objects.filter(Q(user__isnull=True) |
                                                             Q(user=user))


class TagForm(forms.ModelForm):
    class Meta:
        model = TaskTag
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
