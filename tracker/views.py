from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction, Budget
from .forms import TransactionForm
from rest_framework import generics
from .models import Transaction, Budget
from django.contrib.auth.forms import UserCreationForm
from .serializers import TransactionSerializer, BudgetSerializer
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
import uuid

# Create your views here.
#List Transaction view

def login(request):
    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
def landing_page(request):
    return render(request, 'landing.html')

@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transaction_list.html', {'transactions': transactions})

# View for managing the dashboard (only shows buttons now, no transactions)
def transaction_management(request):
    return render(request, 'transaction_management.html')

# View for displaying all transactions in a table
def view_transactions(request):
    transactions = Transaction.objects.all()  # Fetch all transactions
    return render(request, 'view_transactions.html', {'transactions': transactions})  # Pass transactions to template

# View for adding a new transaction
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.save()  # Save and generate ref_id
            return redirect('view_transactions')  # Redirect to the view transactions page after adding
    else:
        form = TransactionForm()  # Empty form for GET requests
    return render(request, 'add_transaction.html', {'form': form})

# View for editing a transaction
def edit_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()  # Save changes
            return redirect('view_transactions')  # Redirect to the view transactions page after editing
    else:
        form = TransactionForm(instance=transaction)  # Prepopulate form with existing transaction data
    return render(request, 'edit_transaction.html', {'form': form})

# View for deleting a transaction
def delete_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    if request.method == 'POST':
        transaction.delete()  # Delete the transaction
        return redirect('view_transactions')  # Redirect back to view transactions page after deletion
    return render(request, 'delete_transaction.html', {'transaction': transaction})

#Budget view
@login_required
def view_budget(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'tracker/view_budget.html', {'budgets': budgets})
# View for Budget Management
def budget_management(request):
    return render(request, 'budget_management.html')

# View for Get Report
def get_report_view(request):
    return render(request, 'get_report.html')
#API Views
class TransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer = TransactionSerializer

class BudgetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer = BudgetSerializer

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
