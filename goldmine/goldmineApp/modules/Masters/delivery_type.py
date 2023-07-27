from goldmineApp . models import Delivery_Type
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required




# @login_required(login_url='admin_login_url')
def fn_Delivery_Type_Add_View(request):
    '''
    This view function for add the new delivery type.
    '''
    if request.method == 'POST':
        s_Delivery_Type  = str.capitalize(request.POST.get('delivery_type'))

        obj = Delivery_Type(
            s_Delivery_Type=s_Delivery_Type
            )

        obj.save()
        return redirect('delivery_type_list_url')

    return render(request,'masters/delivery_type/add.html')


# @login_required(login_url='admin_login_url')
def fn_Delivery_Type_List_View(request):
    '''
    This view function for display all the delivery types.
    '''
    form = Delivery_Type.objects.all()
    context = {'form':form}
    return render(request,'masters/delivery_type/list.html',context)


# @login_required(login_url='admin_login_url')
def fn_Delivery_Type_Update_View(request,id):
    '''
    This view function for update the specific delivery type.
    '''
    obj = Delivery_Type.objects.get(id=id)
    context = {'obj':obj}
    if request.method == 'POST':
        s_Delivery_Type  = str.capitalize(request.POST.get('delivery_type'))

        obj = Delivery_Type(
            id=id,
            s_Delivery_Type=s_Delivery_Type
            )

        obj.save()
        return redirect('delivery_type_list_url')

    return render(request,'masters/delivery_type/update.html',context)


# @login_required(login_url='admin_login_url')
def fn_Delivery_Type_Delete_View(request,id):
    '''
    This view function for delete the specific delivery type.
    '''
    obj = Delivery_Type.objects.get(id=id)
    obj.delete()
    return redirect('delivery_type_list_url')

