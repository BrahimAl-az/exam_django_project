from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Jane Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'jane@example.com'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'I loved the chicken curry...', 'rows': 5}),
        }
