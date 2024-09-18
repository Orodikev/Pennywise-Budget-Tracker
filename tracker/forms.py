from django import forms
from .models import Transaction
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# TransactionForm inherits from ModelForm to handle form rendering for the Transaction model
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction  # Link the form to the Transaction model
        fields = ['amount', 'date', 'category']  # Fields to be included in the form
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),  # Custom styling for the amount input
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # Dropdown date picker
            'category': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for category selection
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
