from django import forms
from .models import Transaction
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Define transaction view
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction  # Reference the existing Transaction model
        fields = ['date', 'category', 'amount']  # Specify the fields to be used
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'category': forms.Select(choices=[
                ('food', 'Food'),
                ('rent', 'Rent'),
                ('transport', 'Transport'),
                ('shopping', 'Shopping'),
                ('clothing', 'Clothing'),
                ('medication', 'Medication'),
            ]),
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
