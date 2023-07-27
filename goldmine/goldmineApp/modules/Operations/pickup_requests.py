from goldmineApp . models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Max,Min,Avg,Sum,Count
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



# @login_required(login_url='admin_login_url')
def fn_Pickup_Request_Add_View(request):
    
    form1 =  Branch.objects.all()
    form2 =  Pay_Type.objects.all()
    consignors = Consignor.objects.all()
    consignees = Consignee.objects.all()

    context = {
        'form1':form1,
        'form2':form2,
        'consignors':consignors,
        'consignees':consignees
        }
    
    if request.method == 'POST':
        i_Pid_No = 1001 if Pickup_Request.objects.count() == 0 else Pickup_Request.objects.aggregate(max=Max('i_Pid_No'))["max"]+1
        i_PR_NO = str(i_Pid_No)
        s_Branch = Branch.objects.filter(s_Branch_City=request.POST.get('branch_city')).first()
        g = str(s_Branch)
        s = g[0:3]
        bid = s.upper() + '_' + i_PR_NO
        # s_Branch = request.POST.get('branch_city')
        s_Pay_Type = Pay_Type.objects.filter(s_Pay_Type=request.POST.get('pay_type')).first()
        s_Consignor_Name = Consignor.objects.filter(s_Consignor_Name=request.POST.get('consignor_name')).first()
        s_Consignee_Name = Consignee.objects.filter(s_Consignee_Name=request.POST.get('consignee_name')).first()     
        s_Date = request.POST.get('date')
        i_No_of_Articles = request.POST.get('no_of_articles')
        s_Consignor_Address=request.POST.get('consignor_address')
        s_Consignor_GST = request.POST.get('consignor_gst')
        s_Consignee_Address = request.POST.get('consignee_address')
        s_Consignee_GST = request.POST.get('consignee_gst')
        s_From = request.POST.get('branch_city')
        s_To = request.POST.get('to')
        s_Description = request.POST.get('description')
        i_Actual_Weight = request.POST.get('actual_weight')
        i_Charged_Weight = request.POST.get('charged_weight')
        i_Freight = request.POST.get('freight')
        i_FOV = request.POST.get('fov')
        i_Docket_Charge = request.POST.get('docket_charge')
        i_Grant_Total = request.POST.get('grant_total')
        s_Remark = request.POST.get('remark')

        p = Pickup_Request(
            s_Date=s_Date,
            i_Pid_No=i_Pid_No,
            s_Pay_Type=s_Pay_Type,
            s_Branch=s_Branch,
            i_PR_NO=bid,
            i_No_of_Articles=i_No_of_Articles,
            s_Consignor_Name=s_Consignor_Name,
            s_Consignor_Address=s_Consignor_Address,
            s_Consignor_GST=s_Consignor_GST,
            s_Consignee_Name=s_Consignee_Name,
            s_Consignee_Address=s_Consignee_Address,
            s_Consignee_GST=s_Consignee_GST,
            s_From=s_From,
            s_To=s_To,
            s_Description=s_Description,
            i_Actual_Weight=i_Actual_Weight,
            i_Charged_Weight=i_Charged_Weight,
            i_Freight=i_Freight,
            i_FOV=i_FOV,
            i_Docket_Charge=i_Docket_Charge,
            i_Grant_Total=i_Grant_Total,
            s_Remark=s_Remark,
            )
        p.save()
        return redirect('pickup_request_list_url')

    return render(request,'add-pickup-request.html',context)



# @login_required(login_url='admin_login_url')
def fn_Pickup_Request_List_View(request):
    '''
    This view function for display all Pickup Request with data.
    '''
    if request.method =="POST":
        fromdate= request.POST.get("from_date")
        todate= request.POST.get("to_date")
        result = Pickup_Request.objects.all().filter(s_Date__range=(fromdate, todate)) 
        context = {'data':result}
        return render(request,'pickup-request-list.html',context)
    else :
        form = Pickup_Request.objects.all()
        paginator = Paginator(form,10)
        page_number = request.GET.get('page')
        form4 = paginator.get_page(page_number)
        context = {'form':form,'form4':form4}
    return render(request,'pickup-request-list.html',context)

  
    


# @login_required(login_url='admin_login_url')
def fn_Pickup_Request_Details_View(request,id):
    obj = Pickup_Request.objects.get(id=id)
    context = {
        'obj':obj,
        'username':obj.i_PR_NO
        }
    return render(request,'pickup_request_preview.html',context)

    

# @login_required(login_url='admin_login_url')
def fn_Pickup_Request_Update_View(request,id):
    '''
    This view function for update the specific Pickup.
    '''
    form1 =  Branch.objects.all()
    form2 =  Pay_Type.objects.all()
    vehicles = Vehicle.objects.all()
    obj = Pickup_Request.objects.get(id=id)
    consignors = Consignor.objects.all()
    consignees = Consignee.objects.all()
    
    context = {
        'form1':form1,
        'form2':form2,
        'vehicles':vehicles,
        'obj':obj,
        'consignors':consignors,
        'consignees':consignees
        }    
    
    if request.method == 'POST':
        i_PR_NO = request.POST.get('i_PR_NO')
        i_Pid_No = request.POST.get('i_Pid_No')
        
        s_Branch = Branch.objects.filter(s_Branch_City=request.POST.get('branch_city')).first()
        s_Pay_Type = Pay_Type.objects.filter(s_Pay_Type=request.POST.get('pay_type')).first()
        s_Consignor_Name = Consignor.objects.filter(s_Consignor_Name=request.POST.get('consignor_name')).first()
        s_Consignee_Name = Consignee.objects.filter(s_Consignee_Name=request.POST.get('consignee_name')).first()
       
       
        s_Date = request.POST.get('date')
        i_No_of_Articles = request.POST.get('i_No_of_Articles')
        s_Consignor_Address=request.POST.get('consignor_address')
        s_Consignor_GST = request.POST.get('consignor_gst')
        s_Consignee_Address = request.POST.get('consignee_address')
        s_Consignee_GST = request.POST.get('consignee_gst')
        s_From = request.POST.get('from')
        s_To = request.POST.get('to')
        s_Description = request.POST.get('description')
        i_Actual_Weight = request.POST.get('actual_weight')
        i_Charged_Weight = request.POST.get('charged_weight')
        i_Freight = request.POST.get('freight')
        i_FOV = request.POST.get('fov')
        i_Docket_Charge = request.POST.get('docket_charge')
        i_Grant_Total = request.POST.get('grant_total')
        s_Vehicle = request.POST.get('vehicle')
        s_Remark = request.POST.get('remark')

        c = Pickup_Request(
            id=id,
            s_Date=s_Date,
            s_Pay_Type=s_Pay_Type,
            s_Branch=s_Branch,
            i_PR_NO=i_PR_NO,
            i_Pid_No=i_Pid_No,
            i_No_of_Articles=i_No_of_Articles,
            s_Consignor_Name=s_Consignor_Name,
            s_Consignor_Address=s_Consignor_Address,
            s_Consignor_GST=s_Consignor_GST,
            s_Consignee_Name=s_Consignee_Name,
            s_Consignee_Address=s_Consignee_Address,
            s_Consignee_GST=s_Consignee_GST,
            s_From=s_From,
            s_To=s_To,
            s_Description=s_Description,
            i_Actual_Weight=i_Actual_Weight,
            i_Charged_Weight=i_Charged_Weight,
            i_Freight=i_Freight,
            i_FOV=i_FOV,
            i_Docket_Charge=i_Docket_Charge,
            i_Grant_Total=i_Grant_Total,
            s_Vehicle=s_Vehicle,
            s_Remark=s_Remark,            
            )
        c.save()
        return redirect('pickup_request_list_url')

    return render(request,'edit-pickup-request.html',context)



# @login_required(login_url='admin_login_url')
def fn_Pickup_Request_Delete_View(request,id):
    '''
    This view function for delete the specific Pickup Request.
    '''
    obj = Pickup_Request.objects.get(id=id)
    obj.delete()
    return redirect('pickup_request_list_url')



########## Code for Consignor Name  with Address & GST ##########
def get_user_info(request,user_name):
    congi = Consignor.objects.get(s_Consignor_Name = user_name)
   
    congi_info = {
        'address': congi.s_Consignor_Address,
        'gst': congi.s_Consignor_GST,
    }
    print(congi_info)
    return JsonResponse(congi_info)




########## Code for Consignee Name  with Address & GST ##########
def get_consi_info(request,consi_name):
    consi = Consignee.objects.get(s_Consignee_Name = consi_name)
   
    consi_info = {
        'consi_address': consi.s_Consignee_Address,
        'consi_gst': consi.s_Consignee_GST,
    }
    return JsonResponse(consi_info)



################### Generate PDF ########################




    



