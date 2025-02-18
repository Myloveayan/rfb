# Generated by Django 5.0.6 on 2024-06-30 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebank', '0008_remove_transaction_account_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='amount',
            new_name='credit',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='transaction_type',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='remark',
        ),
        migrations.AddField(
            model_name='transaction',
            name='debit',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
    ]
