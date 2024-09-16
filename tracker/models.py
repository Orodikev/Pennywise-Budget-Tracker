from django.db import models
import uuid
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

# Transaction model
class Transaction(models.Model):
    # Fields for the transaction
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)

    # Unique reference number for each transaction
    ref_number = models.CharField(max_length=100, unique=True, blank=True, null=True)

    # Overriding the save method to generate a unique ref_number if not provided
    def save(self, *args, **kwargs):
        if not self.ref_number:
            self.ref_number = str(uuid.uuid4())  # Generate a unique UUID for ref_number
        super(Transaction, self).save(*args, **kwargs)

    # String representation of the model
    def __str__(self):
        return f"Transaction {self.ref_number}: {self.category} - {self.amount} on {self.date}"

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

