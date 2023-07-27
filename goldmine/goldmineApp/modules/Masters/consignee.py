from goldmineApp . models import Consignee
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required



# @login_required(login_url='admin_login_url')
def fn_Consignee_Add_View(request):
    '''
    This view function for add the new location.
    '''
    if request.method == 'POST':
        s_Consignee_Name = str.capitalize(request.POST.get('consignee_name'))
        s_Consignee_Address = request.POST.get('consignee_address')
        s_Consignee_GST = request.POST.get('consignee_gst')
        i_Mobile_No = request.POST.get('mobile_no')
        s_State = str.capitalize(request.POST.get('state'))

        obj = Consignee(
            s_Consignee_Name=s_Consignee_Name,
            s_Consignee_Address=s_Consignee_Address,
            s_Consignee_GST=s_Consignee_GST,
            i_Mobile_No=i_Mobile_No,
            s_State=s_State,
            )
        
        obj.save()
        return redirect('consignee_list_url')
    
    return render(request,'masters/consignee/add.html')



# @login_required(login_url='admin_login_url')
def fn_Consignee_List_view(request):
    '''
    This view function for display all locations
    '''
    form = Consignee.objects.all()
    context = {'form':form}
    return render(request,'masters/consignee/list.html',context)




# @login_required(login_url='admin_login_url')
def fn_Consignee_Update_View(request,id):
    '''
    This view function for update the data of specific location.
    '''
    obj = Consignee.objects.get(id=id)
    context = {'obj':obj}
    if request.method == 'POST':
        s_Consignee_Name = str.capitalize(request.POST.get('consignee_name'))
        s_Consignee_Address = request.POST.get('consignee_address')
        s_Consignee_GST = request.POST.get('consignee_gst')
        i_Mobile_No = request.POST.get('mobile_no')
        s_State = str.capitalize(request.POST.get('state'))

        obj = Consignee(
            id=id,
            s_Consignee_Name=s_Consignee_Name,
            s_Consignee_Address=s_Consignee_Address,
            s_Consignee_GST=s_Consignee_GST,
            i_Mobile_No=i_Mobile_No,
            s_State=s_State,
            )
        obj.save()
        return redirect('consignee_list_url')

    return render(request,'masters/consignee/update.html',context)



# @login_required(login_url='admin_login_url')
def fn_Consignee_Delete_View(request,id):
    '''
    This view function for delete the specific location.
    '''
    obj = Consignee.objects.get(id=id)
    obj.delete()
    return redirect('consignee_list_url')

