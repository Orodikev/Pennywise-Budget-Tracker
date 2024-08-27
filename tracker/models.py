from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    INCOME = 'income'
    EXPENSE = 'expense'
    CATEGORY_TYPES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CATEGORY_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount} - {self.category.name} on {self.date}'

class Budget(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Budget for {self.category.name} from {self.start_date} to {self.end_date}'

class Tag(models.Model):
    name = models.CharField(max_length=50)
    transaction = models.ForeignKey(Transaction, related_name='tags', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

