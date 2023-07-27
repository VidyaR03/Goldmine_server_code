from goldmineApp . models import Consignor
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required


# @login_required(login_url='admin_login_url')
def fn_Consignor_Add_View(request):
    '''
    This view function for add the new location.
    '''
    if request.method == 'POST':
        s_Consignor_Name = request.POST.get('consignor_name')
        s_Consignor_Address = request.POST.get('consignor_address')
        s_Consignor_GST = request.POST.get('consignor_gst')
        i_Mobile_No = request.POST.get('mobile_no')
        s_State = request.POST.get('state')

        obj = Consignor(
            s_Consignor_Name=s_Consignor_Name,
            s_Consignor_Address=s_Consignor_Address,
            s_Consignor_GST=s_Consignor_GST,
            i_Mobile_No=i_Mobile_No,
            s_State=s_State,
            )
        
        obj.save()
        return redirect('consignor_list_url')
    
    return render(request,'masters/consignors/add.html')



# @login_required(login_url='admin_login_url')
def fn_Consignor_List_view(request):
    '''
    This view function for display all locations
    '''
    form = Consignor.objects.all()
    context = {'form':form}
    return render(request,'masters/consignors/list.html',context)



# @login_required(login_url='admin_login_url')
def fn_Consignor_Update_View(request,id):
    '''
    This view function for update the data of specific location.
    '''
    obj = Consignor.objects.get(id=id)
    context = {'obj':obj}
    if request.method == 'POST':
        s_Consignor_Name = request.POST.get('consignor_name')
        s_Consignor_Address = request.POST.get('consignor_address')
        s_Consignor_GST = request.POST.get('consignor_gst')
        i_Mobile_No = request.POST.get('mobile_no')
        s_State = request.POST.get('state')

        obj = Consignor(
            id=id,
            s_Consignor_Name=s_Consignor_Name,
            s_Consignor_Address=s_Consignor_Address,
            s_Consignor_GST=s_Consignor_GST,
            i_Mobile_No=i_Mobile_No,
            s_State=s_State,
            )

        obj.save()
        return redirect('consignor_list_url')

    return render(request,'masters/consignors/update.html',context)



# @login_required(login_url='admin_login_url')
def fn_Consignor_Delete_View(request,id):
    '''
    This view function for delete the specific location.
    '''
    obj = Consignor.objects.get(id=id)
    obj.delete()
    return redirect('consignor_list_url')
