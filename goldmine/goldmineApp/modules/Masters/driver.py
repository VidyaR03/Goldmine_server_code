from goldmineApp . models import Driver
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

# @login_required(login_url='admin_login_url')
def fn_Driver_Add_View(request):
    '''
    This view function for add the data of new driver.
    '''
    if request.method == 'POST':
        s_driver_name = str.capitalize(request.POST.get('driver_name'))
        s_date_of_birth = str.capitalize(request.POST.get('driver_dob'))
        s_address = request.POST.get('driver_address')
        s_city = str.capitalize(request.POST.get('driver_city'))
        s_state = str.capitalize(request.POST.get('driver_state'))
        i_mobile_number = request.POST.get('driver_mobile')
        s_licence_number = request.POST.get('driver_licence_number')
        
        d = Driver(
            s_driver_name=s_driver_name,
            s_date_of_birth=s_date_of_birth,
            s_address=s_address,
            s_city=s_city,
            s_state=s_state,
            i_mobile_number=i_mobile_number,
            s_licence_number=s_licence_number
            )
    
        d.save()
        return redirect('driver_list_url')

    return render(request,'masters/drivers/add.html')



# @login_required(login_url='admin_login_url')
def fn_Driver_List_View(request):
    '''
    This view function for display all drivers.
    '''
    form = Driver.objects.all()
    context = {'form':form}
    return render(request,'masters/drivers/list.html',context)


# @login_required(login_url='admin_login_url')
def fn_Driver_Update_View(request,id):
    '''
    This view function for update the data of specific driver.
    '''
    obj = Driver.objects.get(id=id)
    context = {'obj':obj}
    if request.method == 'POST':
        s_driver_name = str.capitalize(request.POST.get('driver_name'))
        s_date_of_birth = request.POST.get('driver_dob')
        s_address = request.POST.get('driver_address')
        s_city = str.capitalize(request.POST.get('driver_city'))
        s_state = str.capitalize(request.POST.get('driver_state'))
        i_mobile_number = request.POST.get('driver_mobile')
        s_licence_number = request.POST.get('driver_licence_number')
        
        d = Driver(
            id=id,
            s_driver_name=s_driver_name,
            s_date_of_birth=s_date_of_birth,
            s_address=s_address, 
            s_city=s_city,
            s_state=s_state,
            i_mobile_number=i_mobile_number,
            s_licence_number=s_licence_number
            )
        
        d.save()
        return redirect('driver_list_url')

    return render(request,'masters/drivers/update.html',context)


# @login_required(login_url='admin_login_url')
def fn_Driver_Delete_View(request,id):
    '''
    This view function for dalete the specific driver.
    '''
    driver = Driver.objects.get(id=id)
    driver.delete()
    return redirect('driver_list_url')
