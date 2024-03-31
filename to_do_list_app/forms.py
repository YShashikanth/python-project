from django import forms
from .models import UniqueTodo
class UniqueTodoForm(forms.ModelForm):
    class Meta:
        model = UniqueTodo
        fields = ['task_name', 'priority', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }