from goldmineApp . models import Location
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required


# @login_required(login_url='admin_login_url')
def fn_Location_Add_View(request):
    '''
    This view function for add the new location.
    '''
    if request.method == 'POST':
        s_Address = request.POST.get('address')
        s_City = str.capitalize(request.POST.get('city'))
        i_PinCode = request.POST.get('pincode')

        l = Location(
            s_Address=s_Address,
            s_City=s_City,
            i_PinCode=i_PinCode
            )
        
        l.save()
        return redirect('location_list_url')
    
    return render(request,'masters/locations/add.html')



# @login_required(login_url='admin_login_url')
def fn_Location_List_view(request):
    '''
    This view function for display all locations
    '''
    form = Location.objects.all()
    context = {'form':form}
    return render(request,'masters/locations/list.html',context)


# @login_required(login_url='admin_login_url')
def fn_Location_Update_View(request,id):
    '''
    This view function for update the data of specific location.
    '''
    obj = Location.objects.get(id=id)
    context = {'obj':obj}
    if request.method == 'POST':
        s_Address = request.POST.get('address')
        s_City = request.POST.get('city')
        i_PinCode = request.POST.get('pincode')

        l = Location(
            id=id,
            s_Address=s_Address,
            s_City=s_City,
            i_PinCode=i_PinCode
            )

        l.save()
        return redirect('location_list_url')

    return render(request,'masters/locations/update.html',context)


# @login_required(login_url='admin_login_url')
def fn_Location_Delete_View(request,id):
    '''
    This view function for delete the specific location.
    '''
    obj = Location.objects.get(id=id)
    obj.delete()
    return redirect('location_list_url')

