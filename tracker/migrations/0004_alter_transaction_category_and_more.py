# Generated by Django 5.1 on 2024-09-17 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_alter_transaction_ref_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('food', 'Food'), ('rent', 'Rent'), ('transport', 'Transport'), ('shopping', 'Shopping'), ('clothing', 'Clothing'), ('medication', 'Medication')], max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='ref_number',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True),
        ),
    ]
