from django.db import models
import uuid # Import for generating unique reference ID
from django.contrib.auth.models import User 
from datetime import date # To default the date to today's date

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
CATEGORY_CHOICES = [
    ('food', 'Food'),
    ('rent', 'Rent'),
    ('transport', 'Transport'),
    ('shopping', 'Shopping'),
    ('clothing', 'Clothing'),
    ('medication', 'Medication'),
]

# Transaction model with fields: ref_id, amount, date, category
class Transaction(models.Model):
   # ref_id = models.CharField(max_length=100, unique=True, editable=False)  # Auto-generated reference ID
    ref_id = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount of transaction
    date = models.DateField(default=date.today)  # Transaction date, default is today
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # Category selection with predefined choices

    # Overriding the save method to generate a unique reference ID if it does not exist
    def save(self, *args, **kwargs):
        if not self.ref_id:
            self.ref_id = str(uuid.uuid4()).split('-')[0]  # Generate a short UUID for ref_id
        super(Transaction, self).save(*args, **kwargs)

    # Return a string representation of the transaction
    def __str__(self):
        return f"{self.ref_id} - {self.amount}"
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

