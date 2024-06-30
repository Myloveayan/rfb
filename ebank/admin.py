# myapp/admin.py

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # Import this class
from .models import Customer, BankAccount, Transaction

@admin.register(Customer, BankAccount, Transaction)
class MyModelAdmin(ImportExportModelAdmin):  # Use ImportExportModelAdmin
    pass
