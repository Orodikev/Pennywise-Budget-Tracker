from django.urls import path, include
from .views import TransactionListCreateAPIView, BudgetListCreateAPIView
from . import views
from django.contrib.auth import views as auth_views
from .views import register
from .views import login
from .views import RegisterView

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.transaction_list, name='transaction_list'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('budget/', views.view_budget, name='view_budget'),
    path('api/transactions/', TransactionListCreateAPIView.as_view(), name='api_transactions'),
    path('api/budgets/', BudgetListCreateAPIView.as_view(), name='api_budgets'),
    path('register/', RegisterView.as_view(), name='register'),
    path('transaction-management/', views.transaction_management_view, name='transaction_management'),
    path('budget-management/', views.budget_management_view, name='budget_management'),
    path('get-report/', views.get_report_view, name='get_report'),
]
