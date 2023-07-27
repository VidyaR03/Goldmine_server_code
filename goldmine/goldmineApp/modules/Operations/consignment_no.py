from goldmineApp . models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.core.paginator import Paginator
from django.http import JsonResponse
import datetime


# @login_required(login_url='admin_login_url')
def fn_Consignment_No_Add_View(request):
    form1 =  Branch.objects.all()
    form2 =  Pay_Type.objects.all()
    form3 = Vehicle.objects.all()
    current_date = datetime.date.today()
    consignors = Consignor.objects.all()
    consignees = Consignee.objects.all()
    context = {
        'form1':form1,
        'form2':form2,
        'form3':form3,
        'consignors':consignors,
        'consignees':consignees,
        'current_date':current_date
        }

    if request.method == 'POST':
        i_Lid_No = 2001 if Consignment_No.objects.count() == 0 else Consignment_No.objects.aggregate(max=Max('i_Lid_No'))["max"]+1
        s_Branch = Branch.objects.filter(s_Branch_City=request.POST.get('branch_city')).first()
        i_LR_NO = str(i_Lid_No)
        g = str(s_Branch)
        s = g[0:3]      
        bid = s.upper() + '_' + i_LR_NO
        s_Pay_Type = Pay_Type.objects.filter(s_Pay_Type=request.POST.get('pay_type')).first()
        s_Consignor_Name = Consignor.objects.filter(s_Consignor_Name=request.POST.get('consignor_name')).first()
        s_Consignee_Name = Consignee.objects.filter(s_Consignee_Name=request.POST.get('consignee_name')).first()    
        
        s_From = request.POST.get('from')
        s_To = request.POST.get('to')        
        s_Date = request.POST.get('date')
        s_Consignor_Address=request.POST.get('s_Consignor_Address')
        print(s_Consignor_Address)
        s_Consignor_GST = request.POST.get('consignor_gst')
        s_Consignee_Address = request.POST.get('consignee_address')
        s_Consignee_GST = request.POST.get('consignee_gst')
        i_No_of_Articles = request.POST.get('no_of_articles')        
        s_Description = request.POST.get('description')
        i_Actual_Weight = request.POST.get('actual_weight')
        i_Charged_Weight = request.POST.get('charged_weight')
        i_Freight = request.POST.get('freight')
        i_FOV = request.POST.get('fov')
        i_Docket_Charge = request.POST.get('docket_charge')
        i_Grant_Total = request.POST.get('grant_total')
        s_Remark = request.POST.get('remark')

        obj = Consignment_No(
            s_Date=s_Date,
            i_Lid_No=i_Lid_No,

            s_Pay_Type=s_Pay_Type,
            s_Branch=s_Branch,

            i_LR_NO = bid,
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
        obj.save()
        return redirect('consignment_no_list_url')

    return render(request,'add-consignment.html',context)




# @login_required(login_url='admin_login_url')
def fn_Consignment_No_List_View(request):
    '''
    This view function for display all Cosignment Entry with data.
    '''
    if request.method =="POST":
        fromdate= request.POST.get("from_date")
        todate= request.POST.get("to_date")
        result = Consignment_No.objects.all().filter(s_Date__range=(fromdate, todate)) 
        return render(request,'consignment-list.html',{'data':result})
    else :
        form = Consignment_No.objects.all()
        paginator = Paginator(form,10)
        page_number = request.GET.get('page')
        form4 = paginator.get_page(page_number)
        context = {'form':form,'form4':form4}
        return render(request,'consignment-list.html',context)





# @login_required(login_url='admin_login_url')
def fn_Consignment_No_Deatails_View(request,id):
    obj = Consignment_No.objects.get(id=id)
    context = {
        'obj':obj,
        'username':obj.i_LR_NO
        }
    return render(request,'consignment-preview.html',context)




# @login_required(login_url='admin_login_url')
def fn_Consignment_No_Update_View(request,id):
    '''
    This view function for update the specific Consignment.
    '''
    form1 =  Branch.objects.all()
    form2 =  Pay_Type.objects.all()

    consignors = Consignor.objects.all()
    consignees = Consignee.objects.all()
    obj = Consignment_No.objects.get(id=id)
    vehicles = Vehicle.objects.all()
    
    context = {
        'form1':form1,
        'form2':form2,
        'consignors':consignors,
        'consignees':consignees,
        'obj':obj,
        'vehicles':vehicles
        }
    
    if request.method == 'POST':
        i_Lid_No = request.POST.get('i_Lid_No')
        i_LR_NO = request.POST.get('i_LR_NO')
        
        
        #i_Lid_No = int(i_LR_NO)
        s_Branch = Branch.objects.filter(s_Branch_City=request.POST.get('branch_city')).first()
        s_Pay_Type = Pay_Type.objects.filter(s_Pay_Type=request.POST.get('pay_type')).first()
        s_Consignor_Name = Consignor.objects.filter(s_Consignor_Name=request.POST.get('consignor_name')).first()
        s_Consignee_Name = Consignee.objects.filter(s_Consignee_Name=request.POST.get('consignee_name')).first()
       
       
        s_Date = request.POST.get('date')
        i_No_of_Articles = request.POST.get('no_of_articles')
        
        s_Consignor_Address = request.POST.get('consignor_address')
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
        s_Vehicle = request.POST.get('vehicle')

        obj = Consignment_No(
            id=id,
            s_Date=s_Date,
            s_Pay_Type=s_Pay_Type,
            s_Branch=s_Branch,
            i_LR_NO=i_LR_NO,
            i_Lid_No=i_Lid_No,
            i_No_of_Articles=i_No_of_Articles,
            s_Consignor_Name=s_Consignor_Name,
            s_Consignee_Name=s_Consignee_Name,
            s_Consignor_Address=s_Consignor_Address,
            s_Consignor_GST=s_Consignor_GST,
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
            s_Vehicle=s_Vehicle
            )
        obj.save()
        return redirect('consignment_no_list_url')

    return render(request,'edit-consignment.html',context)




# @login_required(login_url='admin_login_url')
def fn_Consignment_No_Delete_View(request,id):
    '''
    This view function for delete the specific Pickup Request.
    '''
    obj = Consignment_No.objects.get(id=id)
    obj.delete()
    return redirect('consignment_no_list_url')

# PDF GENERATE CODE 

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def generate_cn_pdf(request,id):
    template = get_template('consignment_pdf.html')
    
    obj = Consignment_No.objects.get(id=id)
 
    context = {'obj':obj,
               'username':obj.i_LR_NO,
                'branch':obj.s_Branch,
                'Date':obj.s_Date,
                'vehicle':obj.s_Vehicle,
                'consignee':obj.s_Consignee_Name,
                'consignee_address':obj.s_Consignee_Address,
                'consignee_gst':obj.s_Consignee_GST,
               
                'consignor':obj.s_Consignor_Name,
                'consignor_address':obj.s_Consignor_Address,
                'consignor_gst':obj.s_Consignor_GST,
               
               }
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Consignment.pdf"'
    # create a pdf object
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response






########## Code for Consignor Name  with Address & GST ##########
def get_user_info(request,user_name):
    congi = Consignor.objects.get(s_Consignor_Name = user_name)
   
    congi_info = {
        'user_address': congi.s_Consignor_Address,
        'user_Gst': congi.s_Consignor_GST,
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

