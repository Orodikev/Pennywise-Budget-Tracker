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
    path('budget/', views.view_budget, name='view_budget'),
    path('api/transactions/', TransactionListCreateAPIView.as_view(), name='api_transactions'),
    path('api/budgets/', BudgetListCreateAPIView.as_view(), name='api_budgets'),
    path('register/', RegisterView.as_view(), name='register'),
    path('transaction-management/', views.transaction_management, name='transaction_management'),
    path('transactions/<str:action>/', views.transaction_management, name='transaction_action'),  # For add/edit/delete actions
    path('transactions/<str:action>/<int:transaction_id>/', views.transaction_management, name='transaction_action_with_id'),  # For edit/delete with ID
    path('budget-management/', views.budget_management, name='budget_management'),
    path('get-report/', views.get_report_view, name='get_report'),
    path('add-transaction/', views.add_transaction, name='add_transaction'),
    path('edit-transaction/<int:id>/', views.edit_transaction, name='edit_transaction'),
    path('delete-transaction/<int:id>/', views.delete_transaction, name='delete_transaction'),
]
