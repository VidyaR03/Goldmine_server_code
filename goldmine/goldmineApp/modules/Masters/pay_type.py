from goldmineApp . models import Pay_Type
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required



# @login_required(login_url='admin_login_url')
def fn_Pay_Type_Add_View(request):
    '''
    This view function for add new pay type.
    '''
    if request.method == 'POST':
        s_Pay_Type = str.capitalize(request.POST.get('pay_type'))

        obj = Pay_Type(
            s_Pay_Type=s_Pay_Type
            )

        obj.save()
        return redirect('pay_type_list_url')

    return render(request,'masters/pay_type/add.html')



# @login_required(login_url='admin_login_url')
def fn_Pay_Type_List_View(request):
    '''
    This view function for display all pay types.
    '''
    form = Pay_Type.objects.all()
    context = {'form':form}
    return render(request,'masters/pay_type/list.html',context)



# @login_required(login_url='admin_login_url')
def fn_Pay_Type_Update_View(request,id):
    '''
    This view function for update the specific pay type.
    '''
    obj = Pay_Type.objects.get(id=id)
    context = {'obj':obj}
    if request.method == 'POST':
        s_Pay_Type = str.capitalize(request.POST.get('pay_type'))

        obj = Pay_Type(
            id=id,
            s_Pay_Type=s_Pay_Type
            )

        obj.save()
        return redirect('pay_type_list_url')

    return render(request,'masters/pay_type/update.html',context)



# @login_required(login_url='admin_login_url')
def fn_Pay_Type_Delete_View(request,id):
    '''
    This view function for  delete specific pay type.
    '''
    obj = Pay_Type.objects.get(id=id)
    obj.delete()
    return redirect('pay_type_list_url')

