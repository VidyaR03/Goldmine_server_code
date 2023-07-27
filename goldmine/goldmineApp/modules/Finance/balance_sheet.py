from django.shortcuts import render,redirect
from goldmineApp . models import *

def fn_balance_sheet_View(request):
   balance = Balance_Sheet.objects.all()
   branch =  Branch.objects.all()
   
   context = {
     'balance':balance,
     'branch':branch,
        
    }
   return render(request,'finance/balance_sheet/list_balance_sheet.html',context)




def create_balance_sheet(request):
    balance = Balance_Sheet.objects.all()
    branch =  Branch.objects.all()

    context = {'balance' : balance,'branch':branch}

    if request.method == 'POST':
        s_Branch = Branch.objects.filter(s_Branch_City=request.POST.get('branch_city')).first()
        liabilities = request.POST.get('liabilities')
        cr_amount = request.POST.get('cr_amount')
        asset = request.POST.get('asset')
        dr_amount = request.POST.get('dr_amount')  

        obj = Balance_Sheet(
            s_Branch = s_Branch,
            liabilities = liabilities, 
            cr_amount = cr_amount,
            asset = asset,
            dr_amount = dr_amount,
            
        )
        obj.save()
        return redirect('balance_sheet_list')
    return render(request,'finance/balance_sheet/add_balance.html',context)



###############


def balance_edit(request, id):
    balance = Balance_Sheet.objects.get(id=id)
    branch =  Branch.objects.all()
    context = {'balance' : balance,'branch':branch}

    if request.method == 'POST':
        s_Branch = Branch.objects.filter(s_Branch_City=request.POST.get('branch_city')).first()
        liabilities = request.POST.get('liabilities')
        cr_amount = request.POST.get('cr_amount')
        asset = request.POST.get('asset')
        dr_amount = request.POST.get('dr_amount')      



        obj = Balance_Sheet(
            id = id,
            s_Branch = s_Branch,
            liabilities = liabilities, 
            cr_amount = cr_amount,
            asset = asset,
            dr_amount = dr_amount,
            
        )
        obj.save()
        return redirect('balance_sheet_list')
    return render(request,'finance/balance_sheet/edit_balance.html',context)


    
# @login_required(login_url='admin_login_url')
def fn_balance_Details_View(request):
    '''
    This view function for display the specific account information.
    '''
    balance = Balance_Sheet.objects.all()
    context = {'balance':balance}
    return render(request,'finance/balance_sheet/details_balance.html',context)


def balance_delete(request, id):
    balance = Balance_Sheet.objects.get(id=id)
    balance.delete()
    return redirect('balance_sheet_list')
   











##########
#/home/vidya/Goldmine_Logistick_06/goldmine