from django.shortcuts import render,redirect
from goldmineApp . models import *

def fn_add_trial_balance(request):
    branch = Branch.objects.all()
    ledger = Ledger.objects.all()

    context = {
        'branch': branch,'ledger':ledger
    }
    if request.method == 'POST':
        s_Branch = Branch.objects.filter(s_Branch_City = request.POST.get('branch_city')).first()
        s_ledger = Ledger.objects.filter(s_ledger_name = request.POST.get('ledger_name')).first()
        opening_debit = request.POST.get('opening_debit')
        opening_credit = request.POST.get('opening_credit')
        transaction_debit = request.POST.get('transaction_debit')
        transaction_credit = request.POST.get('transaction_credit')
        closing_debit = request.POST.get('closing_debit')
        closing_credit = request.POST.get('closing_credit')
        d_date = request.POST.get('d_date')

        
        obj = Trial_Balance(
            s_Branch = s_Branch,
            s_ledger = s_ledger,
            opening_debit = opening_debit,
            opening_credit = opening_credit,
            transaction_debit = transaction_debit,
            transaction_credit = transaction_credit,
            closing_debit = closing_debit,
            closing_credit = closing_credit,
            d_date = d_date
        )
        obj.save()
        return redirect('trial_balance_list')
    return render(request,'finance/trial_balance/add_trial.html',context)


def fn_edit_trial_balance(request,id):
    branch = Branch.objects.all()
    trial = Trial_Balance.objects.get(id=id)
    ledger = Ledger.objects.all()

    context = {
        'branch': branch,'trial':trial,'ledger':ledger
    }
    if request.method == 'POST':
        s_Branch = Branch.objects.filter(s_Branch_City = request.POST.get('branch_city')).first()
        s_ledger = Ledger.objects.filter(s_ledger_name = request.POST.get('ledger_name')).first()
        opening_debit = request.POST.get('opening_debit')
        opening_credit = request.POST.get('opening_credit')
        transaction_debit = request.POST.get('transaction_debit')
        transaction_credit = request.POST.get('transaction_credit')
        closing_debit = request.POST.get('closing_debit')
        closing_credit = request.POST.get('closing_credit')
        d_date = request.POST.get('d_date')

        
        obj = Trial_Balance(
            id=id,
            s_Branch = s_Branch,
            s_ledger = s_ledger,
            opening_debit = opening_debit,
            opening_credit = opening_credit,
            transaction_debit = transaction_debit,
            transaction_credit = transaction_credit,
            closing_debit = closing_debit,
            closing_credit = closing_credit,
            d_date = d_date
        )
        obj.save()
        return redirect('trial_balance_list')
    return render(request,'finance/trial_balance/edit_trial.html',context)

def fn_delete_trial_balance(request,id):
    '''
    This view function for delete the specifice account.
    '''
    trial = Trial_Balance.objects.get(id=id)
    trial.delete()
    return redirect('trial_balance_list')

def fn_list_trial_balance(request):
    '''
    This view function for display the all account information.
    '''
    trial = Trial_Balance.objects.all()
    context = {'trial':trial}
    return render(request,'finance/trial_balance/list_trial.html',context)

    
# @login_required(login_url='admin_login_url')
def fn_trial_Details_View(request,id):
    trial = Trial_Balance.objects.get(id=id)
    ledger = Ledger.objects.filter(s_ledger_name=id)
    
    
    
    context = {
        'trial':trial,
        'ledger':ledger,
        
    }
    
    return render(request,'finance/trial_balance/details_trial.html',context)












