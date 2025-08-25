from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'comments'] #Fields to display
        widgets = {
            'comments':forms.Textarea(attrs={'rows':4, 'placeholder':'Write your feedback here.'})
        }