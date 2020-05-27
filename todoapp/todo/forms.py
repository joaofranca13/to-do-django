from django import forms
from .models import AddTask


class SubmitNewTask(forms.ModelForm):
    task = forms.CharField(max_length=200)

    class Meta:
        model = AddTask
        fields = ['task']
