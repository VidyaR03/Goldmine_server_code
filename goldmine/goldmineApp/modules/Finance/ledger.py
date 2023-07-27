from django.shortcuts import render, get_object_or_404, redirect
from goldmineApp . models import *


def create_ledger(request):
    group = Group.objects.all()
    context = {'group' : group}

    if request.method == 'POST':
        s_ledger_name = request.POST.get('s_ledger_name')
        s_Group = Group.objects.filter(s_Group_Name=request.POST.get('group_name')).first()
        s_ac_name = request.POST.get('ac_holder_name')
        s_ac_no = request.POST.get('s_ac_no')
        s_ifsc_code = request.POST.get('ifsc_code')
        s_swift_code = request.POST.get('swift_code')
        s_bank_name = request.POST.get('bank_name')
        s_branch_name = request.POST.get('branch_name')
        t_branch_address = request.POST.get('branch_address')
        s_under = request.POST.get('s_under')
        s_tax_type = request.POST.get('s_tax_type')
        d_percentage = request.POST.get('d_percentage')
        d_rounding = request.POST.get('d_rounding')
        s_name = request.POST.get('s_name')
        t_address = request.POST.get('t_address')
        i_mobile_no = request.POST.get('i_mobile_no')
        s_state = request.POST.get('s_state')
        s_country = request.POST.get('s_country')
        d_date = request.POST.get('d_date')



        obj = Ledger(
            s_ledger_name = s_ledger_name,
            s_Group = s_Group, 
            s_ac_name = s_ac_name, 
            s_ac_no = s_ac_no,
            s_ifsc_code = s_ifsc_code,
            s_swift_code = s_swift_code,
            s_bank_name = s_bank_name,
            s_branch_name = s_branch_name,
            t_branch_address = t_branch_address,
            s_under = s_under,
            s_tax_type = s_tax_type,
            d_percentage = d_percentage,
            d_rounding = d_rounding,
            s_name = s_name,
            t_address = t_address,
            i_mobile_no = i_mobile_no,
            s_state = s_state, 
            s_country = s_country,
            d_date = d_date     

        )
        obj.save()
        return redirect('ledger_list')
    return render(request,'finance/ledger_account/create_ledger.html',context)



###############


def ledger_edit(request, id):
    ledger = Ledger.objects.get(id=id)
    group = Group.objects.all()
    context = {'group' : group, 'ledger':ledger}

    if request.method == 'POST':
        s_ledger_name = request.POST.get('s_ledger_name')
        s_Group = Group.objects.filter(s_Group_Name=request.POST.get('group_name')).first()
        s_ac_name = request.POST.get('ac_holder_name')
        s_ac_no = request.POST.get('s_ac_no')
        s_ifsc_code = request.POST.get('ifsc_code')
        s_swift_code = request.POST.get('swift_code')
        s_bank_name = request.POST.get('bank_name')
        s_branch_name = request.POST.get('branch_name')
        t_branch_address = request.POST.get('branch_address')
        s_under = request.POST.get('s_under')
        s_tax_type = request.POST.get('s_tax_type')
        d_percentage = request.POST.get('d_percentage')
        d_rounding = request.POST.get('d_rounding')
        s_name = request.POST.get('s_name')
        t_address = request.POST.get('t_address')
        i_mobile_no = request.POST.get('i_mobile_no')
        s_state = request.POST.get('s_state')
        s_country = request.POST.get('s_country')
        d_date = request.POST.get('d_date')



        obj = Ledger(
            id=id,
            s_ledger_name = s_ledger_name,
            s_Group = s_Group, 
            s_ac_name = s_ac_name, 
            s_ac_no = s_ac_no,
            s_ifsc_code = s_ifsc_code,
            s_swift_code = s_swift_code,
            s_bank_name = s_bank_name,
            s_branch_name = s_branch_name,
            t_branch_address = t_branch_address,
            s_under = s_under,
            s_tax_type = s_tax_type,
            d_percentage = d_percentage,
            d_rounding = d_rounding,
            s_name = s_name,
            t_address = t_address,
            i_mobile_no = i_mobile_no,
            s_state = s_state, 
            s_country = s_country,
            d_date = d_date         

        )
        obj.save()
        return redirect('ledger_list')
    return render(request,'finance/ledger_account/edit_ledger.html',context)

def ledger_List_View(request):
    '''
    This view function for display the all ledger information.
    '''
    ledger = Ledger.objects.all()
    context = {'ledger':ledger}
    return render(request,'finance/ledger_account/ledger_list.html',context)

    
# @login_required(login_url='admin_login_url')
def fn_ledger_Details_View(request,id):
    '''
    This view function for display the specific account information.
    '''
    ledger = Ledger.objects.get(id=id)
    context = {'ledger':ledger}
    return render(request,'finance/ledger_account/details.html',context)


def ledger_delete(request, id):
    ledger = Ledger.objects.get(id=id)
    ledger.delete()
    return redirect('ledger_list')
   











##########
#/home/vidya/Goldmine_Logistick_06/goldmine