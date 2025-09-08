from django import forms
from .models import Feedback
from .models import ContactSubmission

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'comments'] #Fields to display
        widgets = {
            'comments':forms.Textarea(attrs={'rows':4, 'placeholder':'Write your feedback here.'})
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email'] #Only show these two fields to user
        #Add bootstrap styling
        widgets = {
            'name':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Enter your name'}),
            'email':forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'Enter your email'}),
        }
