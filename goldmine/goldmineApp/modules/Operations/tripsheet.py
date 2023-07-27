from goldmineApp. models import Trip_Sheet, Branch, Vehicle, Driver,Location,Consignor,Manifest_Load
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.http import JsonResponse



# @login_required(login_url='admin_login_url')
def fn_Trip_Sheet_List_View(request):
    form = Trip_Sheet.objects.all()
    context = {'form':form}
    return render(request,'tripsheet_list.html',context)



# @login_required(login_url='admin_login_url')
def fn_Trip_Sheet_Add_View(request):
   
    form1 = Branch.objects.all()
    form2 = Vehicle.objects.all()
    form3 = Driver.objects.all()
    form4 = Location.objects.all()
    form5 = Consignor.objects.all()
    form6 = Manifest_Load.objects.all()
    try:
        latest_trip_sheet_id = Trip_Sheet.objects.latest('id')
        next_id = latest_trip_sheet_id.i_Trip_Sheet_No + 1
    except:
        next_id = 1

 
    context = {
        'form1':form1,
        'form2':form2,
        'form3':form3,
        'form4':form4,
        'form5':form5,
        'form6':form6,
        'next_id':next_id
    }
    if request.method == 'POST':

        i_Trip_Sheet_No =  1001 if Trip_Sheet.objects.count() == 0 else Trip_Sheet.objects.aggregate(max=Max('i_Trip_Sheet_No'))["max"]+1
        i_TR_NO = str(i_Trip_Sheet_No)
        s_Branch = Branch.objects.filter(s_Branch_City= request.POST.get('branch_city')).first()
        print(s_Branch.s_Branch_City)
        g = str(s_Branch)
        s = g[0:3]
        tid = s.upper() + '_' + i_TR_NO


        s_To = request.POST.get('to') 
        s_Via =  request.POST.get('via') 
        s_Vehicle = Vehicle.objects.filter(s_vehicle_number=request.POST.get('vehicle')).first()
        s_Driver1 = Driver.objects.filter(s_driver_name=request.POST.get('driver1')).first()
        s_Driver2 = request.POST.get('driver2') 
        #i_Manifest_No = request.POST.get('manifest_no') 
        i_Total_Packages = request.POST.get('packages') 
        i_Total_Weight = request.POST.get('total_weight') 

        s_Start_Date = request.POST.get('s_date') 
        i_Loaded_Weight = request.POST.get('loaded_weight') 
        s_Party_Name = request.POST.get('party_name') 
        i_Opening_KM = request.POST.get('opening_km') 
        i_Advance_to_Driver = request.POST.get('advance_to_driver') 
        
        s_Sign_of_Authority = request.POST.get('sign_of_authority') 
        # pr = request.POST.getlist('prid')
        # i_PR_NO = ''
        # for i in pr:
        #     i_PR_NO += str(i) + ',' 
        # print(i_PR_NO)    
        tm = request.POST.getlist('manifest_no')
        i_Manifest_No = ''
        for i in tm:
             i_Manifest_No += str(i) + ',' 
        # print(i_PR_NO) 
        
        

        
        

        obj = Trip_Sheet(

            i_Trip_Sheet_No=i_Trip_Sheet_No,
            i_TR_NO=tid,
            s_Branch=s_Branch,
            s_To=s_To,
            s_Via=s_Via,
            s_Vehicle=s_Vehicle,
            s_Driver1=s_Driver1,
            s_Driver2=s_Driver2,
            i_Manifest_No=i_Manifest_No,
            i_Total_Packages=i_Total_Packages,
            i_Total_Weight=i_Total_Weight,
            i_Advance_to_Driver=i_Advance_to_Driver,
            
            s_Start_Date=s_Start_Date,
            i_Loaded_Weight=i_Loaded_Weight,
            s_Party_Name=s_Party_Name,
            i_Opening_KM=i_Opening_KM,
                    
            s_Sign_of_Authority=s_Sign_of_Authority,
            
        )
        obj.save()
        return redirect('trip_sheet_list_url')

    return render(request,'add_tripsheet.html',context)



# @login_required(login_url='admin_login_url')
def fn_Trip_Sheet_Details_View(request,id):
    obj = Trip_Sheet.objects.get(id=id)
    context = {'obj':obj}
    return render(request,'tripsheet-preview.html',context)



# @login_required(login_url='admin_login_url')
def fn_Trip_Sheet_Update_View(request,id):
    print("called")
    form1 = Branch.objects.all()
    form2 = Vehicle.objects.all()
    form3 = Driver.objects.all()
    obj = Trip_Sheet.objects.get(id=id)
    form5 = Consignor.objects.all()
    form6 = Manifest_Load.objects.all()

    context = {
        'form1':form1,
        'form2':form2,
        'form3':form3,
        'obj':obj,
        'form5':form5,
        'form6':form6
    }
    if request.method == 'POST':

        i_Trip_Sheet_No = request.POST.get('i_Trip_Sheet_No')
        i_TR_NO=request.POST.get('i_TR_NO')
        s_Branch = Branch.objects.filter(s_Branch_City= request.POST.get('branch')).first()
        s_To = request.POST.get('to') 
        s_Via =  request.POST.get('via') 
        s_Vehicle = Vehicle.objects.filter(s_vehicle_number=request.POST.get('vehicle')).first()
        s_Driver1 = Driver.objects.filter(s_driver_name=request.POST.get('driver1')).first()
        s_Driver2 = request.POST.get('driver2') 
        #i_Manifest_No = request.POST.get('manifest_no') 
        i_Total_Packages = request.POST.get('packages') 
        i_Total_Weight = request.POST.get('total_weight') 
         
        s_Start_Date = request.POST.get('s_date')
        s_End_Date = request.POST.get('e_date') 
        i_Loaded_Weight = request.POST.get('loaded_weight') 
        s_Party_Name = request.POST.get('party_name') 
        i_Opening_KM = request.POST.get('opening_km') 
        s_Reach_Date = request.POST.get('reach_date') 
        s_Reach_Time = request.POST.get('reach_time') 
        i_Closing_KM = request.POST.get('closing_km') 
        i_Total_Running_KM = request.POST.get('total_run_km') 
        i_Total_Hours = request.POST.get('total_hours') 
        i_Disel_Issued = request.POST.get('diesel_issued') 
        i_Disel_Rate = request.POST.get('diesel_rate_first') 
        i_Average = request.POST.get('average_km') 
        i_Advance_to_Driver = request.POST.get('advance_to_driver') 
        s_Sign_of_Authority = request.POST.get('sign_of_authority') 
        
        i_Total_Disel_Qty = request.POST.get('total_diesel_qty') 
        i_Rate_Per_KM = request.POST.get('rate_km') 
        i_Total_Amt = request.POST.get('total_amt') 

        i_Disel = request.POST.get('diesel_ltrs_second') 
        print(i_Disel)
        i_Cash_Toll = request.POST.get('cash_toll') 
        i_Entry_Tax = request.POST.get('entry_tax') 
        i_Border_Tax = request.POST.get('border_tax') 
        i_Vehicle_Repair = request.POST.get('vehicle_repair') 
        i_Loading_Unloading = request.POST.get('loading_unloading') 
        i_Others = request.POST.get('others') 
        i_Total_Expence = request.POST.get('total_expence') 
        print(i_Total_Expence)
        i_Advance = request.POST.get('total_advance') 
        i_Total_Amount = request.POST.get('total_amount') 

        i_Disel_LTRS = request.POST.get('diesel_ltrs_last') 
        i_Disel_Rate_Last = request.POST.get('diesel_rate_last') 
        i_Total_Disel_Cost = request.POST.get('total_diesel_cost') 

        s_Remark = request.POST.get('remark') 
        tm = request.POST.getlist('manifest_no')
        i_Manifest_No = ''
        for i in tm:
             i_Manifest_No += str(i) + ',' 

        obj = Trip_Sheet(
            id=id,
            i_Trip_Sheet_No=i_Trip_Sheet_No,
            i_TR_NO=i_TR_NO,
            s_Branch=s_Branch,
            s_To=s_To,
            s_Via=s_Via,
            s_Vehicle=s_Vehicle,
            s_Driver1=s_Driver1,
            s_Driver2=s_Driver2,
            i_Manifest_No=i_Manifest_No,
            i_Total_Packages=i_Total_Packages,
            i_Total_Weight=i_Total_Weight,
            s_Start_Date=s_Start_Date,
            s_End_Date=s_End_Date,
            i_Loaded_Weight=i_Loaded_Weight,
            s_Party_Name=s_Party_Name,
            i_Opening_KM=i_Opening_KM,
            s_Reach_Date=s_Reach_Date,
            s_Reach_Time=s_Reach_Time,
            i_Closing_KM=i_Closing_KM,
            i_Total_Running_KM=i_Total_Running_KM,
            i_Total_Hours=i_Total_Hours,
            i_Disel_Issued=i_Disel_Issued,
            i_Disel_Rate=i_Disel_Rate,
            i_Average=i_Average,
            i_Advance_to_Driver=i_Advance_to_Driver,
            s_Sign_of_Authority=s_Sign_of_Authority,
            i_Total_Disel_Qty=i_Total_Disel_Qty,
            i_Rate_Per_KM=i_Rate_Per_KM,
            i_Total_Amt=i_Total_Amt,
            i_Disel=i_Disel,
            i_Cash_Toll=i_Cash_Toll,
            i_Entry_Tax=i_Entry_Tax,
            i_Border_Tax=i_Border_Tax,
            i_Vehicle_Repair=i_Vehicle_Repair,
            i_Loading_Unloading=i_Loading_Unloading,
            i_Others=i_Others,
            i_Total_Expence=i_Total_Expence,
            i_Advance=i_Advance,
            i_Total_Amount=i_Total_Amount,
            i_Disel_LTRS=i_Disel_LTRS,
            i_Disel_Rate_Last=i_Disel_Rate_Last,
            i_Total_Disel_Cost=i_Total_Disel_Cost,
            s_Remark=s_Remark
        )
        obj.save()
        return redirect('trip_sheet_list_url')

    return render(request,'edit-tripsheet.html',context)



# @login_required(login_url='admin_login_url')
def fn_Trip_Sheet_Delete_View(request,id):
    obj = Trip_Sheet.objects.get(id=id)
    obj.delete()
    return redirect('trip_sheet_list_url')


########## Code for add amanifest number with pkg and weight ##########
def get_mani_info(request,mani_no):
    mani = Manifest_Load.objects.get(s_Manifest_No = mani_no)
   
    mani_info = {
        'mani_pkg': mani.i_Package,
        'mani_weight': mani.i_Weight,
    }
    return JsonResponse(mani_info)




