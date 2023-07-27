from goldmineApp . models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


# @login_required(login_url='admin_login_url')
def fn_Vehicle_Add_View(request):

   

    form_d = Driver.objects.all()
    print(form_d)
    context = {'form_d': form_d}

    if request.method == 'POST':
        s_vehicle_number = request.POST.get('vehicle_number')
        s_vehicle_type = request.POST.get('vehicle_type')
        s_driver_name = str.capitalize(request.POST.get('vehicle_driver_name'))
        i_driver_mobile = request.POST.get('vehicle_driver_mobile')
        s_owner_name = str.capitalize(request.POST.get('vehicle_owner_name'))
        i_owner_mobile = request.POST.get('vehicle_owner_mobile')
        s_owner_pan_number = request.POST.get('vehicle_owner_pan_number')

        # Check if driver with given name already exists
        driver = get_object_or_404(Driver, s_driver_name=s_driver_name)

        # Create a new driver if it doesn't exist
        if not driver:
            driver = Driver(s_driver_name=s_driver_name)
            driver.save()

        vehicle = Vehicle(
            s_vehicle_number=s_vehicle_number,
            s_vehicle_type=s_vehicle_type,
            s_Driver_name=driver,
            i_driver_mobile=i_driver_mobile,
            s_owner_name=s_owner_name,
            i_owner_mobile=i_owner_mobile,
            s_owner_pan_number=s_owner_pan_number
        )
        vehicle.save()
        return redirect('vehicle_list_url')

    return render(request, 'masters/vehicle/add.html', context)


# @login_required(login_url='admin_login_url')
def fn_Vehicle_List_View(request):
    '''
    This view function for display all vehicles with data.
    '''
    form = Vehicle.objects.all()
    context = {'form':form}
    return render(request,'masters/vehicle/list.html',context)



# @login_required(login_url='admin_login_url')
def fn_Vehicle_Update_View(request,s_vehicle_number):
    '''
    This view function for update the the data of specific vehicle.
    '''
    # form_d =  Driver.objects.all()
    # print(form_d)
    # context = {'form_d':form_d}
    # vehicle = Vehicle.objects.get(s_vehicle_number=s_vehicle_number)
    # context = {'vehicle':vehicle}
    # if request.method == 'POST':
    #     s_vehicle_number = request.POST.get('vehicle_number')
    #     s_vehicle_type = request.POST.get('vehicle_type')
    #     s_Driver_name = Driver.objects.filter(s_driver_name=request.POST.get('vehicle_driver_name')).first()
    #     i_driver_mobile = request.POST.get('vehicle_driver_mobile')
    #     s_owner_name = request.POST.get('vehicle_owner_name')
    #     i_owner_mobile = request.POST.get('vehicle_owner_mobile')
    #     s_owner_pan_number = request.POST.get('vehicle_owner_pan_number')

    #     v = Vehicle(
    #         s_vehicle_number=s_vehicle_number,
    #         s_vehicle_type=s_vehicle_type,
    #         s_Driver_name=s_Driver_name,
    #         i_driver_mobile=i_driver_mobile,
    #         s_owner_name=s_owner_name,
    #         i_owner_mobile=i_owner_mobile,
    #         s_owner_pan_number=s_owner_pan_number
    #         )
        
    #     v.save()
    #     return redirect('vehicle_list_url')

    # return render(request,'masters/vehicle/update.html',context)
    drivers = Driver.objects.all()
    vehicle = get_object_or_404(Vehicle, s_vehicle_number=s_vehicle_number)
    context = {'vehicle':vehicle}

    if request.method == 'POST':
        s_vehicle_number = request.POST.get('vehicle_number')
        s_vehicle_type = request.POST.get('vehicle_type')
        s_Driver_name = Driver.objects.filter(s_driver_name=request.POST.get('vehicle_driver_name')).first()
        i_driver_mobile = request.POST.get('vehicle_driver_mobile')
        s_owner_name = str.capitalize(request.POST.get('vehicle_owner_name'))
        i_owner_mobile = request.POST.get('vehicle_owner_mobile')
        s_owner_pan_number = request.POST.get('vehicle_owner_pan_number')

        v = Vehicle(
            s_vehicle_number=s_vehicle_number,
            s_vehicle_type=s_vehicle_type,
            s_Driver_name=s_Driver_name,
            i_driver_mobile=i_driver_mobile,
            s_owner_name=s_owner_name,
            i_owner_mobile=i_owner_mobile,
            s_owner_pan_number=s_owner_pan_number
        )

        v.save()
        return redirect('vehicle_list_url')

    context = {'form_d': drivers, 'vehicle': vehicle}
    return render(request, 'masters/vehicle/update.html', context)




# @login_required(login_url='admin_login_url')
def fn_Vehicle_Delete_View(request,s_vehicle_number):
    '''
    This view function for delete the specific vehicle.
    '''
    form = Vehicle.objects.get(s_vehicle_number=s_vehicle_number)
    form.delete()
    return redirect('vehicle_list_url')
