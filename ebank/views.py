from django.shortcuts import render, redirect
from .forms import SignUpForm, CustomerForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Customer, BankAccount, Transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('login')




class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('account_created')
    template_name = 'registration/open_account.html'

import json
import csv
from django.shortcuts import render

def transaction_history(request):
    transactions = []

    # Replace 'path_to_your_csv_file.csv' with the actual path to your CSV file
    with open('C:/Users/Abbati/Documents/RFBank/data/history.csv', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            transactions.append(row)

    # Render the template with the transactions data
    return render(request, 'ebank/transaction_history.html', {'transactions': transactions})

import csv
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import BankAccount

@login_required
def bank_accounts(request):
    transactions = []
    bank_accounts = BankAccount.objects.filter(user=request.user)

    # Adjust path according to your actual file location
    csv_file_path = 'C:/Users/Abbati/Documents/RFBank/data/preview.csv'

    try:
        with open(csv_file_path, newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                transactions.append(row)
    except FileNotFoundError:
        # Handle file not found error appropriately
        # For example, raise an exception or provide a default behavior
        pass

    return render(request, 'ebank/bank_accounts.html', {
        'bank_accounts': bank_accounts,
        'transactions': transactions
    })



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})




def login(request):
    return render(request,'ebank/login.html')

@login_required
def dashboard(request):
    return render(request,'ebank/dashboard.html')

@login_required
def myaccounts(request):
    return render(request,'ebank/myaccounts.html')
@login_required
def accountstatement(request):
    return render(request,'ebank/accountstatement.html')
@login_required
def rfbtransfer(request):
    return render(request,'ebank/rfbtransfer.html')
@login_required
def otherbankstransfer(request):
    return render(request,'ebank/otherbankstransfer.html')
@login_required
def internationaltransfer(request):
    return render(request,'ebank/internationaltransfer.html')
@login_required
def spendanalysis(request):
    return render(request,'ebank/spendanalysis.html')
@login_required
def Cheque(request):
    return render(request,'ebank/Cheque.html')
@login_required
def westernunioun(request):
    return render(request,'ebank/westernunioun.html')
@login_required
def loansummarry(request):
    return render(request,'ebank/loansummary.html')
@login_required
def requestloan(request):
    return render(request,'ebank/requestloan.html')
@login_required
def stopcheque(request):
    return render(request,'ebank/stopcheque.html')
@login_required
def preconfirmcheque(request):
    return render(request,'ebank/preconfirmcheque.html')
@login_required
def viewclearingchequedebt(request):
    return render(request,'ebank/viewclearingchequedebt.html')
@login_required
def Chequedept(request):
    return render(request,'ebank/Chequedept.html')
@login_required
def requestcheque(request):
    return render(request,'ebank/requestcheque.html')
@login_required
def cardreward(request):
    return render(request,'ebank/cardreward.html')
@login_required
def requestcard(request):
    return render(request,'ebank/requestcard.html')
@login_required
def stopcard(request):
    return render(request,'ebank/stopcard.html')
@login_required
def selfservice(request):
    return render(request,'ebank/selfservice.html')
@login_required
def informationupdate(request):
    return render(request,'ebank/informationupdate.html')
@login_required
def passwordsettings(request):
    return render(request,'ebank/passwordsettings.html')
