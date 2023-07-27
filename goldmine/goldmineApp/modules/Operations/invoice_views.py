from goldmineApp. models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.http import JsonResponse

'''*********************************************************************************'''
# Invoice views
'''*********************************************************************************'''

def fn_Invoice_List_View(request):
    '''
    This view function for display all Invoice.
    ''' 
    form = Invoice.objects.all()
    context = {'form':form}      
    
    return render(request,'invoice_list.html',context)


def fn_Invoice_Add_Datewise_View(request):
    '''
    This view function for add datewise.
    '''
    if request.method == 'POST':
        s_Consignor_Name = request.POST.get('consignor')

        
        r = Invoice(
            s_Consignor_Name=s_Consignor_Name,
            
           
            )

        r.save()
        return redirect('invoice_add_url')

    return render(request,'add_invoice.html')



def fn_Invoice_Add_View(request):
    '''
      this view function is for add Invoice.
    '''
    form2 = Consignment_No.objects.all()
    form3 =  Consignor.objects.all()
    form1 =  Branch.objects.all()
    form5 = Vehicle.objects.all()
    
    # form4 = Consignment_No.objects.filter(s_Status=0)
    i_Invoice_Bill = 6001 if Invoice.objects.count() == 0 else Invoice.objects.aggregate(max=Max('i_Invoice_Bill'))["max"]+1

    context = {'form2':form2,'form5':form5,'form1':form1 ,'form3':form3,'i_Invoice_Bill':i_Invoice_Bill}
    if request.method == 'POST':
        #s_Branch = Branch.objects.filter(s_Branch_City= request.POST.get('branch_city')).first()
        
        # i_Bill_No = request.POST.get('bill_no')
        i_Invoice_Bill = 6001 if Invoice.objects.count() == 0 else Invoice.objects.aggregate(max=Max('i_Invoice_Bill'))["max"]+1

        s_Bill_Date  = request.POST.get('bill_date')
        #i_Total_Amount = request.POST.get('total_amt')
        s_GST_No = request.POST.get('gst_no')
        s_Company_GST_No = request.POST.get('company_gst_no')
        s_Company_Pan_No = request.POST.get('company_pan_no')
        s_Company_SAC_No = request.POST.get('company_sac_no')
        s_Consignor_Name = Consignor.objects.filter(s_Consignor_Name= request.POST.get('consignor_name')).first()
        
        s_Consignor_Address = request.POST.get('consignor_address')
        s_Consignor_GST = request.POST.get('consignor_gst')
        #s_State = request.POST.get('state')
        i_Sub_Total = float(request.POST.get('sub_total'))
        s_GST = request.POST.get('gsta')
        i_GST_Amount = request.POST.get('gst_amount')
        i_Total_Final_Amount = float(request.POST.get('total_final_amt'))
        s_Remark = request.POST.get('remark')
        s_Kind_Attention = request.POST.get('kind_attention')
        i_Bill_No = str(i_Invoice_Bill)
        s_Branch = Branch.objects.filter(s_Branch_City=request.POST.get('branch_city')).first()
        d = str(s_Branch)
        s = d[0:3]
        i_Bill_No = s.upper() + '_' + i_Bill_No
        # print(did)

        # inv = request.POST.getlist('cnid')
        # i_Inv=''
        # for i in inv:
        #     i_Inv += str(i) + ','
        

        m = Invoice(
            i_Invoice_Bill=i_Invoice_Bill,
            # i_Inv=i_Inv,
            s_Branch=s_Branch,
            i_Bill_No=i_Bill_No,
            s_Bill_Date=s_Bill_Date,
            #i_Total_Amount=i_Total_Amount,
            s_GST_No=s_GST_No,
            s_Company_GST_No=s_Company_GST_No,
            s_Company_Pan_No=s_Company_Pan_No,
            s_Company_SAC_No=s_Company_SAC_No,
            s_Consignor_Name=s_Consignor_Name,
            s_Consignor_Address=s_Consignor_Address,
            s_Consignor_GST=s_Consignor_GST,
            #s_State=s_State,
            i_Sub_Total=i_Sub_Total,
            s_GST=s_GST,
            i_GST_Amount=i_GST_Amount,
            i_Total_Final_Amount=i_Total_Final_Amount,
            s_Remark=s_Remark,
            s_Kind_Attention=s_Kind_Attention
            )

        m.save()
        id = Invoice.objects.get(i_Invoice_Bill=i_Invoice_Bill).id
        invoice = Invoice.objects.get(id=id)
        value = request.POST.getlist('cnid')
        for val in value:
            obj = Consignment_No.objects.get(id=val)
            obj.i_Invoice_Bill_id = invoice.id
            obj.s_Status = True

            obj.save()

        Invoice.objects.filter(id=id).update(
            s_Consignor_Name=s_Consignor_Name
        )
        return redirect('invoice_list_url')

    return render(request,'add_invoice.html',context)


def fn_Invoice_Update_View(request, id):
    '''
    This view function is for updating an Invoice.
    '''
    form2 = Consignment_No.objects.all()
    form3 = Consignor.objects.all()
    form1 = Branch.objects.all()
    form5 = Vehicle.objects.all()
    obj = Invoice.objects.get(id=id)
    obj2 = Consignment_No.objects.filter(i_Invoice_Bill=id)
    form4 = Consignment_No.objects.filter(s_Status=0)
   


    context = {'form2': form2, 'form5': form5, 'form1': form1, 'form3': form3, 'obj': obj,'obj2':obj2,'form4':form4}

    if request.method == 'POST':
        for x in form4:
            Consignment_No.objects.filter(id=x.id).update(
            i_Invoice_Bill=None,
            s_Status = False
            )
        s_Branch = Branch.objects.filter(s_Branch_City=request.POST.get('branch_city')).first()
        s_Bill_Date = request.POST.get('bill_date')
        s_GST_No = request.POST.get('gst_no')
        s_Company_GST_No = request.POST.get('company_gst_no')
        s_Company_Pan_No = request.POST.get('company_pan_no')
        s_Company_SAC_No = request.POST.get('company_sac_no')
        s_Consignor_Name = Consignor.objects.filter(s_Consignor_Name=request.POST.get('consignor_name')).first()
        s_Consignor_Address = request.POST.get('consignor_address')
        s_Consignor_GST = request.POST.get('consignor_gst')
        i_Sub_Total = float(request.POST.get('sub_total'))
        s_GST = request.POST.get('gst')
        i_GST_Amount = request.POST.get('gst_amt')
        i_Total_Final_Amount = float(request.POST.get('total_final_amt'))
        s_Remark = request.POST.get('remark')
        s_Kind_Attention = request.POST.get('kind_attention')
        i_Bill_No = obj.i_Bill_No  # Retrieve the existing i_Bill_No from the object

        # inv = request.POST.getlist('cnid')
        # i_Inv = ''
        # for i in inv:
        #     i_Inv += str(i) + ','

        # obj.i_Inv = i_Inv
        obj.s_Branch = s_Branch
        obj.i_Bill_No = i_Bill_No
        obj.s_Bill_Date = s_Bill_Date
        obj.s_GST_No = s_GST_No
        obj.s_Company_GST_No = s_Company_GST_No
        obj.s_Company_Pan_No = s_Company_Pan_No
        obj.s_Company_SAC_No = s_Company_SAC_No
        obj.s_Consignor_Name = s_Consignor_Name
        obj.s_Consignor_Address = s_Consignor_Address
        obj.s_Consignor_GST = s_Consignor_GST
        obj.i_Sub_Total = i_Sub_Total
        obj.s_GST = s_GST
        obj.i_GST_Amount = i_GST_Amount
        obj.i_Total_Final_Amount = i_Total_Final_Amount
        obj.s_Remark = s_Remark
        obj.s_Kind_Attention = s_Kind_Attention

        obj.save()
        invoice = Invoice.objects.get(id=id)
        value = request.POST.getlist('cnid')
        for val in value:
            obj = Consignment_No.objects.get(id=val)
            obj.i_Invoice_Bill = invoice
            obj.s_Status = True

            obj.save()

        Invoice.objects.filter(id=id).update(
            s_Consignor_Name=s_Consignor_Name
        )

        return redirect('invoice_list_url')

    return render(request, 'edit-invoice-list.html', context)


def fn_Invoice_Details_View(request,id):
    invoice = Invoice.objects.get(id=id)
    form = Consignment_No.objects.filter(i_Invoice_Bill=id)
    
    context = {
        'invoice':invoice,
        'form':form,
    }

    return render(request,'invoice-list-preview.html',context)




# def fn_Invoice_Details_View(request,id):
#     obj = Invoice.objects.get(id=id)
#     inv = obj.i_Inv.split(',')
#     list = []
#     for i in range(len(inv)-1):
#         data = Consignment_No.objects.filter(i_LR_NO = (inv[i])).first()
#         list.append(data)
    
#     context = {
#         'obj':obj,
#         'pr_no':inv,
#         'list' : list
    
#         }
#     return render(request,'invoice-list-preview.html',context)



# @login_required(login_url='admin_login_url')
def fn_Invoice_Delete_View(request,id):
    '''
    This view function for delete the specific Pickup Request.
    '''
    obj = Invoice.objects.get(id=id)
    obj.delete()
    return redirect('invoice_list_url')




########## Code for Consignor Name  with Address & GST ##########
def get_user_info(request,user_name):
    congi = Consignor.objects.get(s_Consignor_Name = user_name)
   
    congi_info = {
        'address': congi.s_Consignor_Address,
        'gst': congi.s_Consignor_GST,
    }
    print(congi_info)
    return JsonResponse(congi_info)