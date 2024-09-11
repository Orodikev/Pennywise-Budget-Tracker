from django.shortcuts import render, redirect
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

@login_required
#Add Transaction view
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'tracker/add_transaction.html', {'form': form})

#Budget view
@login_required
def view_budget(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'tracker/view_budget.html', {'budgets': budgets})
# View for Transaction Management
def transaction_management_view(request):
    return render(request, 'transaction_management.html')

# View for Budget Management
def budget_management_view(request):
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
