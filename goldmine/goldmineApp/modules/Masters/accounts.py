from goldmineApp . models import Accounts, Group
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required



# @login_required(login_url='admin_login_url')
def fn_Account_Add_View(request):
    '''
    This view function for add account information.
    '''
    form = Group.objects.all()
    context = {'form':form}
    if request.method == 'POST':
        s_Group = Group.objects.filter(s_Group_Name=request.POST.get('group_name')).first()
        s_Company_Name = str.capitalize(request.POST.get('company_name'))
        s_First_Name = str.capitalize(request.POST.get('first_name'))
        s_Last_Name = str.capitalize(request.POST.get('last_name'))
        i_Mobile_Number = request.POST.get('mobile_number')
        i_Phone_Number = request.POST.get('phone_number')
        s_Email_Id = request.POST.get('email_id')
        s_Address = request.POST.get('address')
        s_City = str.capitalize(request.POST.get('city'))
        s_State = str.capitalize(request.POST.get('state'))
        i_PinCode = request.POST.get('pincode')
        i_Fax_Number = request.POST.get('fax_number')
        s_GST_Number = request.POST.get('gst_number')
        s_PAN_Number = request.POST.get('pan_number')

        obj = Accounts(
            s_Group=s_Group,
            s_Company_Name=s_Company_Name,
            s_First_Name=s_First_Name,
            s_Last_Name=s_Last_Name,
            i_Mobile_Number=i_Mobile_Number,
            i_Phone_Number=i_Phone_Number,
            s_Email_Id=s_Email_Id,
            s_Address=s_Address,
            s_City=s_City,
            s_State=s_State,
            i_PinCode=i_PinCode,
            i_Fax_Number=i_Fax_Number,
            s_GST_Number=s_GST_Number,
            s_PAN_Number=s_PAN_Number
            )
        
        obj.save()
        return redirect('account_list_url')
    
    return render(request,'masters/accounts/add.html',context)


# @login_required(login_url='admin_login_url')
def fn_Account_List_View(request):
    '''
    This view function for display the all account information.
    '''
    form = Accounts.objects.all()
    context = {'form':form}
    return render(request,'masters/accounts/list.html',context)

    
# @login_required(login_url='admin_login_url')
def fn_Account_Details_View(request,id):
    '''
    This view function for display the specific account information.
    '''
    obj = Accounts.objects.get(id=id)
    context = {'obj':obj}
    return render(request,'masters/accounts/details.html',context)


# @login_required(login_url='admin_login_url')
def fn_Account_Update_View(request,id):
    '''
    This view function for update the specific account information.
    '''
    form = Group.objects.all()
    obj = Accounts.objects.get(id=id)
    context = {'form':form,'obj':obj}
    if request.method == 'POST':
        s_Group = Group.objects.filter(s_Group_Name=request.POST.get('group_name')).first()
        s_Company_Name = str.capitalize(request.POST.get('company_name'))
        s_First_Name = str.capitalize(request.POST.get('first_name'))
        s_Last_Name = str.capitalize(request.POST.get('last_name'))
        i_Mobile_Number = request.POST.get('mobile_number')
        i_Phone_Number = request.POST.get('phone_number')
        s_Email_Id = request.POST.get('email_id')
        s_Address = request.POST.get('address')
        s_City = str.capitalize(request.POST.get('city'))
        s_State = str.capitalize(request.POST.get('state'))
        i_PinCode = request.POST.get('pincode')
        i_Fax_Number = request.POST.get('fax_number')
        s_GST_Number = request.POST.get('gst_number')
        s_PAN_Number = request.POST.get('pan_number')

        obj = Accounts(
            id=id,
            s_Group=s_Group,
            s_Company_Name=s_Company_Name,
            s_First_Name=s_First_Name,
            s_Last_Name=s_Last_Name,
            i_Mobile_Number=i_Mobile_Number,
            i_Phone_Number=i_Phone_Number,
            s_Email_Id=s_Email_Id,
            s_Address=s_Address,
            s_City=s_City,
            s_State=s_State,
            i_PinCode=i_PinCode,
            i_Fax_Number=i_Fax_Number,
            s_GST_Number=s_GST_Number,
            s_PAN_Number=s_PAN_Number
            )
        
        obj.save()
        return redirect('account_list_url')
    
    return render(request,'masters/accounts/update.html',context)


# @login_required(login_url='admin_login_url')
def fn_Account_Delete_View(request,id):
    '''
    This view function for delete the specifice account.
    '''
    obj = Accounts.objects.get(id=id)
    obj.delete()
    return redirect('account_list_url')
