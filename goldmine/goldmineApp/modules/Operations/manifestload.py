from goldmineApp . models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Max,Min,Avg,Sum,Count
from django.core.paginator import Paginator
import datetime
#from goldmine.settings import localhost
from django.urls import reverse


def fn_Add_Manifest_View(request):
    form = Consignment_No.objects.filter(s_Status=1)
    form1 = Branch.objects.all()
    form2 = Vehicle.objects.all()
    form3 = Location.objects.all()
    current_date = datetime.date.today()
    context = {
        'form': form,
        'form1': form1,
        'form2': form2,
        'form3':form3,
        'current_date': current_date
    }

    if request.method == 'POST':
        i_Manifest_Int = 5001 if Manifest_Load.objects.count() == 0 else Manifest_Load.objects.aggregate(
            max=Max('i_Manifest_Int'))["max"] + 1
        s_vehicle_number = request.POST.get('vehicle_number')
        s_Date = request.POST.get('current_date')
        s_Branch = request.POST.get('branch_city')
        num = str(i_Manifest_Int)
        g = str(s_Branch)
        s = g[0:3]
        s_Manifest_No = s.upper() + '_' + num

        i_Package = 0
        i_Weight = 0

        m = Manifest_Load(
            s_Date=s_Date,
            s_vehicle_number=s_vehicle_number,
            s_Branch=s_Branch,
            i_Manifest_Int=i_Manifest_Int,
            s_Manifest_No=s_Manifest_No,
        )
        m.save()
        id = Manifest_Load.objects.get(i_Manifest_Int=i_Manifest_Int).id
        print(id)
        manifest = Manifest_Load.objects.get(id=id)

        value = request.POST.getlist('consignments')
        for val in value:
            obj = Consignment_No.objects.get(id=val)
            obj.i_Manifest = manifest
            i_Package += obj.i_No_of_Articles
            i_Weight += obj.i_Actual_Weight
            obj.s_Status = True
            obj.i_Mani_NO = manifest.s_Manifest_No
            obj.save()

        Manifest_Load.objects.filter(id=id).update(
            i_Package=i_Package,
            i_Weight=i_Weight
        )

        # # Code for Pickup Runsheet filtering
        # from_location = request.POST.get("from_location")
        # to_location = request.POST.get("to_location")
        # result = Pickup_Runsheet.objects.filter(
        #     from_location__icontains=from_location,
        #     to_location__icontains=to_location
        # )
        # pickup_runsheet_data = {'data': result}
        # context.update(pickup_runsheet_data)
        # End of Pickup Runsheet filtering

        return redirect('manifest_load_list_url')

    return render(request, 'manifest_load_add.html', context)



# @login_required(login_url='admin_login_url')
# def fn_Add_Manifest_View(request):
#     form = Consignment_No.objects.filter(s_Status=0)
#     form1 =  Branch.objects.all()
#     form2 = Vehicle.objects.all()
#     current_date = datetime.date.today()
#     context = {
#         'form':form,
#         'form1':form1,
#         'form2':form2,
#         'current_date':current_date
#         }
#     if request.method == 'POST':
#         i_Manifest_Int = 5001 if Manifest_Load.objects.count() == 0 else Manifest_Load.objects.aggregate(max=Max('i_Manifest_Int'))["max"]+1
#         s_vehicle_number = request.POST.get('vehicle_number')
#         s_Date = request.POST.get('current_date')
#         s_Branch = request.POST.get('branch_city')
#         num = str(i_Manifest_Int)
#         g = str(s_Branch)
#         s = g[0:3]
#         s_Manifest_No = s.upper() + '_' + num

#         i_Package = 0
#         i_Weight = 0
    
#         m = Manifest_Load(
#             s_Date=s_Date, 
#             s_vehicle_number=s_vehicle_number,
#             s_Branch=s_Branch,
#             i_Manifest_Int=i_Manifest_Int,
#             s_Manifest_No=s_Manifest_No,
#             )
#         m.save()
#         id = Manifest_Load.objects.get(i_Manifest_Int=i_Manifest_Int).id
#         print(id)
#         manifest = Manifest_Load.objects.get(id=id)
        
#         value = request.POST.getlist('consignments')
#         for val in value:
#             obj = Consignment_No.objects.get(id=val)
#             obj.i_Manifest = manifest
#             i_Package += obj.i_No_of_Articles
#             i_Weight += obj.i_Actual_Weight
#             obj.s_Status = True
#             obj.i_Mani_NO = manifest.s_Manifest_No
#             obj.save()

#         Manifest_Load.objects.filter(id=id).update(
#             i_Package=i_Package,
#             i_Weight=i_Weight
#         )

#         return redirect('manifest_load_list_url')

#     return render(request,'manifest_load_add.html',context)




# @login_required(login_url='admin_login_url')
def fn_Manifest_Load_List_View(request):
    '''
    This view function for display all Manifest Load List.
    ''' 
    form = Manifest_Load.objects.filter(s_Status=False)
   
    context = {
        'form':form
        }
    
    return render(request,'manifest_list.html',context)





# @login_required(login_url='admin_login_url')
def fn_Manifest_Update_View(request,id):
    '''
      this view function is for add Manifest.
    '''
    obj = Manifest_Load.objects.get(id=id)
    obj2 = Consignment_No.objects.filter(i_Manifest=id)
    
    form = Consignment_No.objects.filter(s_Status=0)
    form1 =  Branch.objects.all()
    form2 = Vehicle.objects.all()
    current_date = datetime.date.today()

    context = {
        'obj':obj,
        'obj2':obj2,
        'form':form,
        'form1':form1,
        'form2':form2,
        'current_date':current_date
        }
    
    if request.method == 'POST':
        for x in obj2:
            Consignment_No.objects.filter(id=x.id).update(
                i_Manifest = None,
                s_Status = False
            )
        s_vehicle_number =request.POST.get('vehicle_number')
        s_Manifest_No =request.POST.get('manifest_no')
        s_Date=request.POST.get('current_date')
        s_Branch = request.POST.get('branch_city')
        i_Package = 0
        i_Weight = 0

        i_Manifest_Int=obj.i_Manifest_Int

        m = Manifest_Load(
            id=id,
            i_Manifest_Int=i_Manifest_Int,
            s_Date=s_Date, 
            s_vehicle_number=s_vehicle_number,
            s_Branch=s_Branch,
            s_Manifest_No=s_Manifest_No,
            )
        m.save()

        manifest = Manifest_Load.objects.get(id=id)
        
        value = request.POST.getlist('consignments')
        for val in value:
            obj = Consignment_No.objects.get(id=val)
            obj.i_Manifest = manifest
            i_Package += obj.i_No_of_Articles
            i_Weight += obj.i_Actual_Weight
            obj.s_Status = True
            obj.save()

        Manifest_Load.objects.filter(id=id).update(
            i_Package=i_Package,
            i_Weight=i_Weight
        )

        return redirect('manifest_load_list_url')

    return render(request,'manifest_load_update.html',context)



# @login_required(login_url='admin_login_url')
def fn_Manifest_Details_View(request,id):
    manifest = Manifest_Load.objects.get(id=id)
    form = Consignment_No.objects.filter(i_Manifest=id)
    context = {
        'manifest':manifest,
        'form':form
    }
    
    return render(request,'manifest_load_details.html',context)


def fetch_data(request):
    from_location = request.GET.get("from_location")
    to_location = request.GET.get("to_location")

    if from_location and to_location:
        data = Consignment_No.objects.filter(from_location=from_location, to_location=to_location)
    else:
        data = Consignment_No.objects.all()

    return render(request, 'your_template.html', {'data': data})





# @login_required(login_url='admin_login_url')
def fn_Manifest_Delete_View(request,id):
    '''
    This view function for delete the specific Manifest.
    '''
    manifest = Manifest_Load.objects.get(id=id)
    consignment = Consignment_No.objects.filter(i_Manifest=manifest.id)
    for obj in consignment:
        Consignment_No.objects.filter(id=obj.id).update(
            i_Manifest = None,
            s_Status = 0
        )

    manifest.delete()
    return redirect('manifest_load_list_url')

