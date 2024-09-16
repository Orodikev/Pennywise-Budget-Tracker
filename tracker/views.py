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
    return render(request, 'tracker/transaction_list.html', {'transactions': transactions})

#Transaction management view
def transaction_management(request):
    # Add Transaction logic
    if request.method == 'POST' and 'add_transaction' in request.POST:
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_management')

    # View all transactions
    transactions = Transaction.objects.all()

    context = {
        'transactions': transactions,
        'form': TransactionForm(),
    }
    return render(request, 'transaction_management.html', context)

def edit_transaction(request, id):
    # Fetch the transaction object or return a 404 if not found
    transaction = get_object_or_404(Transaction, id=id)

    # If this is a POST request, process the form data
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()  # Save the updated transaction
            return redirect('transaction_management')  # Redirect to transaction management page

    # If this is a GET request, display the form prefilled with the transaction details
    else:
        form = TransactionForm(instance=transaction)

    # Render the form for editing the transaction
    return render(request, 'edit_transaction.html', {'form': form})

def delete_transaction(request, id):
    # Fetch the transaction object by ID or return a 404 if not found
    transaction = get_object_or_404(Transaction, id=id)

    # If the request method is POST, delete the transaction
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_management')  # Redirect to transaction management page

    # Render a confirmation page (optional)
    return render(request, 'delete_transaction.html', {'transaction': transaction})

def add_transaction(request):
    if request.method == 'POST':
        date = request.POST['date']
        amount = request.POST['amount']
        category = request.POST['category']

        # Create a new Transaction instance without specifying the ref_number
        transaction = Transaction(date=date, amount=amount, category=category)
        transaction.save()  # This will automatically generate a unique ref_number

        return redirect('transaction_management')

    # Render the template for adding a transaction
    return render(request, 'add_transaction.html')

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
