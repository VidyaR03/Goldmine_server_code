
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.http import JsonResponse
from goldmineApp. models import *
from django.core.paginator import Paginator
import datetime
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from datetime import datetime
from django.core import serializers
import json 
  







def fn_Delivery_Runsheet_List_View(request):
    '''
    This view function for display all Pickup Runsheet with pickup data data.
    '''
    if request.method =="POST":
        fromdate= request.POST.get("from_date")
        todate= request.POST.get("to_date")
        result = Delivery_Run.objects.all().filter(s_Date__range=(fromdate, todate)) 
        context = {'data':result}
        return render(request,'delivery_run_sheet_list.html',context)
    else :
        form = Delivery_Run.objects.all()
        form3 = Branch.objects.all()
        form5 = Location.objects.all()
        paginator = Paginator(form,10)
        page_number = request.GET.get('page')
        form4 = paginator.get_page(page_number)
        context = {'form':form,'form4':form4,'form3':form3,'form5':form5}
        return render(request,'delivery_run_sheet_list.html',context)
    

def new_add(request):
    '''
    This view function for add new Delivery_Runsheet.
    '''  
    form4 = Delivery_Run.objects.all()
    form = Consignment_No.objects.all()
    form1 =  Branch.objects.all()
    form5 = Vehicle.objects.all()
    form3 = Driver.objects.all()
    #datex = datetime.date.today()
    context = {'form':form,'form1':form1,'form3':form3,'form4':form4,'form5':form5}
    if request.method == 'POST':
        # i_Delivery_Runsheet_No = request.objects.filter('i_Delivery_Runsheet_No')
        s_Date = request.POST.get('date')
        i_Delivery_Runsheet_No = 4001 if Delivery_Run.objects.count() == 0 else Delivery_Run.objects.aggregate(max=Max('i_Delivery_Runsheet_No'))["max"]+1
        # i_Delivery_Runsheet_No = request.POST.get('delivery_runsheet_no')
        s_vehicle_number = Vehicle.objects.filter(s_vehicle_number=request.POST.get('vehicle_number')).first()
        s_driver_name = Driver.objects.filter(s_driver_name=request.POST.get('driver_name')).first()     
        s_From = request.POST.get('from')
        s_To = request.POST.get('to')
        s_No_Delivery_Boy = request.POST.get('no_delivery_boy')
        s_Delivery_Boy_Name = request.POST.get('delivery_boy_name')
        i_Delivery_Boy_Phone_No = request.POST.get('delivery_boy_phone_no')
        i_DR_No = str(i_Delivery_Runsheet_No)
        s_Branch = Branch.objects.filter(s_Branch_City=request.POST.get('branch_city')).first()
        d = str(s_Branch)
        s = d[0:3]
        did = s.upper() + '_' + i_DR_No
        # dr = request.POST.getlist('drid')
        # i_DR_No = ''
        # for i in dr:
        #     i_DR_No += str(i) + ',' 
     
        obj = Delivery_Run(
            s_Date=s_Date,
            i_DR_No=did,
            i_Delivery_Runsheet_No=i_Delivery_Runsheet_No,
            s_vehicle_number=s_vehicle_number,
            s_driver_name=s_driver_name,
            s_From=s_From,
            s_To=s_To,
            s_No_Delivery_Boy=s_No_Delivery_Boy,
            s_Delivery_Boy_Name=s_Delivery_Boy_Name,
            i_Delivery_Boy_Phone_No=i_Delivery_Boy_Phone_No,
            s_Branch=s_Branch,
            
            )
        obj.save()
        id = Delivery_Run.objects.get(i_Delivery_Runsheet_No=i_Delivery_Runsheet_No).id
        delivery_runsheet = Delivery_Run.objects.get(id=id)
        value = request.POST.getlist('drid')
        for val in value:
            obj = Consignment_No.objects.get(id=val)
            obj.i_delivery_runsheet = delivery_runsheet
            obj.s_Status = 1
            obj.save()

        Delivery_Run.objects.filter(id=id).update(
            s_vehicle_number=s_vehicle_number
        )

        return redirect('delivery_runsheet_list_url')

    return render(request,'add_delivery_run_sheet.html',context)    

# def new_add(request):
#     '''
#     This view function for add new Delivery_Runsheet.
#     '''
#     form4 = Delivery_Run.objects.all()
#     form = Consignment_No.objects.all()
#     form1 =  Branch.objects.all()
#     form5 = Vehicle.objects.all()
#     form3 = Driver.objects.all()
#     #datex = datetime.date.today()
#     context = {'form':form,'form1':form1,'form3':form3,'form4':form4,'form5':form5}
#     if request.method == 'POST':
#         # i_Delivery_Runsheet_No = request.objects.filter('i_Delivery_Runsheet_No')
#         s_Date = request.POST.get('date')
#         i_Delivery_Runsheet_No = 4001 if Delivery_Run.objects.count() == 0 else Delivery_Run.objects.aggregate(max=Max('i_Delivery_Runsheet_No'))["max"]+1
#         print(i_Delivery_Runsheet_No)
#         # i_Delivery_Runsheet_No = request.POST.get('delivery_runsheet_no')
#         s_vehicle_number = Vehicle.objects.filter(s_vehicle_number=request.POST.get('vehicle_number')).first()
#         s_driver_name = Driver.objects.filter(s_driver_name=request.POST.get('driver_name')).first()
#         s_From = request.POST.get('from')
#         s_To = request.POST.get('to')
#         s_No_Delivery_Boy = request.POST.get('no_delivery_boy')
#         s_Delivery_Boy_Name = request.POST.get('delivery_boy_name')
#         i_Delivery_Boy_Phone_No = request.POST.get('delivery_boy_phone_no')
#         i_DR_No = str(i_Delivery_Runsheet_No)
#         s_Branch = Branch.objects.filter(s_Branch_City=request.POST.get('branch_city')).first()
#         d = str(s_Branch)
#         s = d[0:3]
#         did = s.upper() + '_' + i_DR_No
#         # dr = request.POST.getlist('drid')
#         # i_DR_No = ''
#         # for i in dr:
#         #     i_DR_No += str(i) + ','
#         obj = Delivery_Run(
#             s_Date=s_Date,
#             i_DR_No=did,
#             i_Delivery_Runsheet_No=i_Delivery_Runsheet_No,
#             s_vehicle_number=s_vehicle_number,
#             s_driver_name=s_driver_name,
#             s_From=s_From,
#             s_To=s_To,
#             s_No_Delivery_Boy=s_No_Delivery_Boy,
#             s_Delivery_Boy_Name=s_Delivery_Boy_Name,
#             i_Delivery_Boy_Phone_No=i_Delivery_Boy_Phone_No,
#             s_Branch=s_Branch,
#             )
#         obj.save()
#         id = Delivery_Run.objects.get(i_Delivery_Runsheet_No=i_Delivery_Runsheet_No).id
#         delivery_runsheet = Delivery_Run.objects.get(id=id)
#         value = request.POST.getlist('drid')
#         for val in value:
#             obj = Consignment_No.objects.get(id=val)
#             obj.i_delivery_runsheet = delivery_runsheet
#             obj.s_Status = 1
#             obj.save()
#         Delivery_Run.objects.filter(id=id).update(
#             s_vehicle_number=s_vehicle_number
#         )
#         return redirect('delivery_runsheet_list_url')
#     return render(request,'add_delivery_run_sheet.html',context)

# def fn_Delivery_Runsheet_List_of_consignment_View(request):
#     '''
#       this view function is for list all pickup request with checkbox.
#     '''
#     form4 = Delivery_Run.objects.all()
#     form = Consignment_No.objects.all()
#     form1 =  Branch.objects.all()
#     form5 = Vehicle.objects.all()
#     form3 = Driver.objects.all()
#     # datex = datetime.date.today()

#     context = {'form':form,'form1':form1,'form5':form5,'form3':form3,'form4':form4}
#     if request.method == 'POST':
        
       
#         i_Delivery_Runsheet_No = 4001 if Delivery_Run.objects.count() == 0 else Delivery_Run.objects.aggregate(max=Max('i_Delivery_Runsheet_No'))["max"]+1

#         s_vehicle_number = Vehicle.objects.filter(s_vehicle_number=request.POST.get('vehicle_number')).first()
#         s_driver_name = Driver.objects.filter(s_driver_name=request.POST.get('driver_name')).first()     
#         s_Date = request.POST.get('date')
#         s_From = request.POST.get('branch_city')
#         s_To = request.POST.get('s_To')
#         i_Total_Amount = float(request.POST.get('total_amount', 0))
#         s_No_Delivery_Boy = request.POST.get('s_No_Delivery_Boy')
#         s_Delivery_Boy_Name = request.POST.get('s_Delivery_Boy_Name')
#         i_Delivery_Boy_Phone_No = request.POST.get('i_Delivery_Boy_Phone_No')
#         i_DR_No = str(i_Delivery_Runsheet_No)
#         s_Branch = Branch.objects.filter(s_Branch_City=request.POST.get('branch_city')).first()
#         d = str(s_Branch)
#         s = d[0:3]
#         did = s.upper() + '_' + i_DR_No
#         # dr = request.POST.getlist('drid')
#         # i_DR_No = ''
#         # for i in dr:
#         #     i_DR_No += str(i) + ',' 
        
        
#         obj = Delivery_Run(
#             s_Date=s_Date,
#             i_Delivery_Runsheet_No=i_Delivery_Runsheet_No,
#             s_vehicle_number=s_vehicle_number,
#             i_Delivery_Boy_Phone_No=i_Delivery_Boy_Phone_No,
#             s_No_Delivery_Boy=s_No_Delivery_Boy,
#             s_Delivery_Boy_Name=s_Delivery_Boy_Name,
#             s_From=s_From,
#             s_To=s_To,
#             i_Total_Amount = i_Total_Amount,
#             s_driver_name=s_driver_name,
#             s_Branch=s_Branch,
#             i_DR_No = did,
#             )
#         obj.save()
#         id = Delivery_Run.objects.get(i_Delivery_Runsheet_No=i_Delivery_Runsheet_No).id
#         delivery_runsheet = Delivery_Run.objects.get(id=id)
#         value = request.POST.getlist('drid')
#         for val in value:
#             obj = Consignment_No.objects.get(id=val)
#             obj.i_delivery_runsheet = delivery_runsheet
#             obj.s_Status = True
#             obj.save()

#         Delivery_Run.objects.filter(id=id).update(
#             s_vehicle_number=s_vehicle_number
#         )

#         # return JsonResponse({'success': True})

#         return redirect('delivery_runsheet_list_url')


#     return render(request,'delivery_run_sheet_list.html',context)


def fn_all_report(request):
    '''
    This view function for delete the specific Pickup Request.
    '''
   
    return render(request,'report.html')


def fn_Delivery_Runsheet_Delete_View(request,id):
    '''
    This view function for delete the specific Pickup Request.
    '''
    obj = Delivery_Run.objects.get(id=id)
    obj.delete()
    return redirect('delivery_runsheet_list_url')

# @login_required(login_url='admin_login_url')


def fn_Delivery_Runsheet_Update_View(request,id):
    # form4 = Delivery_Run.objects.all()
    form = Consignment_No.objects.filter(s_Status=0)
    obj = Delivery_Run.objects.get(id=id)
    form1 =  Branch.objects.all()
    form5 = Vehicle.objects.all()
    obj2 = Consignment_No.objects.filter(i_delivery_runsheet=id)
    form3 = Driver.objects.all()
    # dr = obj.i_DR_No.split(',')
    # list = []
    # for i in range(len(dr)-1):
    #     data = Consignment_No.objects.filter(i_LR_NO = (dr[i])).first()
    #     list.append(data)
    
    context = {
        'obj':obj,
        'form':form,
        'form1':form1,
        'form5':form5,
        'form3':form3,
        # 'dr_no':dr,
        # 'list' : list,
        'obj2':obj2,

        } 


    if request.method == 'POST':
        for x in obj2:
            Consignment_No.objects.filter(id=x.id).update(
                i_delivery_runsheet=None,
                s_Status = False
            )

        i_Delivery_Runsheet_No = request.POST.get('i_Delivery_Runsheet_No')
        i_DR_No = request.POST.get('i_DR_No')
        s_vehicle_number = Vehicle.objects.filter(s_vehicle_number=request.POST.get('vehicle_number')).first()
        s_driver_name = Driver.objects.filter(s_driver_name=request.POST.get('driver_name')).first()     
        s_Date = request.POST.get('date')
        s_From = request.POST.get('branch_city')
        s_To = request.POST.get('s_To')
        i_Total_Amount = float(request.POST.get('total_amount', 0))
        s_No_Delivery_Boy = request.POST.get('s_No_Delivery_Boy')
        s_Delivery_Boy_Name = request.POST.get('s_Delivery_Boy_Name')
        i_Delivery_Boy_Phone_No = request.POST.get('i_Delivery_Boy_Phone_No')
        s_Branch = request.POST.get('branch_city')
        dr = request.POST.getlist('drid')
        d = Delivery_Run(
            id=id,
            s_Date=s_Date,
            i_Delivery_Runsheet_No = i_Delivery_Runsheet_No,
            i_DR_No =i_DR_No,
            s_vehicle_number=s_vehicle_number,
            i_Delivery_Boy_Phone_No=i_Delivery_Boy_Phone_No,
            s_No_Delivery_Boy=s_No_Delivery_Boy,
            s_Delivery_Boy_Name=s_Delivery_Boy_Name,
            s_From=s_From,
            s_To=s_To,
            i_Total_Amount = i_Total_Amount,
            s_driver_name=s_driver_name,
            s_Branch=s_Branch,
            )
        d.save()
        # return JsonResponse({'success': True})

        delivery_runsheet = Delivery_Run.objects.get(id=id)
        
        value = request.POST.getlist('drid')

        for val in value:
            obj = Consignment_No.objects.get(id=val)
            obj.i_delivery_runsheet = delivery_runsheet
            obj.s_Status = True
            obj.save()
        Delivery_Run.objects.filter(id=id).update(
            s_vehicle_number = s_vehicle_number
        )

        return redirect('delivery_runsheet_list_url')


    return render(request,'edit_delivery_run_sheet.html',context)   



def fn_Delivery_Runsheet_Details_View(request,id):
    delivery_runsheet = Delivery_Run.objects.get(id=id)
    form = Consignment_No.objects.filter(i_delivery_runsheet=id)
    context = {
        'delivery_runsheet':delivery_runsheet,
        'form':form
    }
    
    return render(request,'delivery-run-sheet-preview.html',context)





    # obj = Delivery_Run.objects.get(id=id)
    # dr = obj.i_DR_No.split(',')
    # list = []
    # for i in range(len(dr)-1):
    #     data = Consignment_No.objects.filter(i_LR_NO = (dr[i])).first()
    #     list.append(data)
    
    # context = {
    #     'obj':obj,
    #     'dr_no':dr,
    #     'list' : list
    
    #     }

    # return render(request,'delivery-run-sheet-preview.html',context)

    
# PDF GENERATE CODE 

def generate_invoice_dpdf(request,id):
    template = get_template('Operations/Delivery_Runsheet/dpdf.html')
    obj = Delivery_Run.objects.get(id=id)
    dr = obj.i_DR_No.split(',')
    list = []
    for i in range(len(dr)-1):
        data = Consignment_No.objects.filter(i_LR_NO = (dr[i])).first()
        list.append(data)
    context = {
               'obj':obj,
                'dr_no':dr,
                'list' : list,
                'date':obj.s_Date,
                'delivery_runsheet_no':obj.i_Delivery_Runsheet_No,
                'branch':obj.s_Branch,
                'vehicle_number':obj.s_vehicle_number,

                'stotal':obj.i_Total_Amount,


                
                # 'lr_no':obj.i_LR_NO,
            #    'consignee':obj.s_Consignee_Name,
            #    'weight':obj.i_Actual_Weight,
            #    'pkg':obj.i_No_of_Articles,
            #    'pay_type':obj.s_Pay_Type,
            #    'amount':obj.i_Grant_Total,
               

              
               }
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Delivery_Run.pdf"'
    # create a pdf object
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# def generate_dpdf(request):
#     template = get_template('Operations/Delivery_Runsheet/pdff.html')
   
#     context = {'my_variable': 'Hello World!'}
#     html = template.render(context)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="Delivery_Runsheet.pdf"'
#     # create a pdf object
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     # if error then show some funy view
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response
    

   
def addconsignment(request):
    if request.method == "POST":
        list_id = request.POST.getlist('id[]')
        vech_id = request.POST.get('v')
        vech = Vehicle.objects.filter(id=vech_id).first()
  
        for i in list_id:
            vl = Delivery_Run.objects.filter(id=i).first()
            vl.save()
    return redirect('delivery_runsheet_list_url',{'vech':vech})


def run_get_consi_no_info(request, consi_no):
    consi = Consignment_No.objects.get(i_LR_NO=consi_no)
    consi_infoo = {
        'consignee': consi.s_Consignee_Name,
        'package': consi.i_No_of_Articles,
        'weight': consi.i_Actual_Weight,
        'paytype': consi.s_Pay_Type,
        'amount': consi.i_Grant_Total,
    }
    print(consi_infoo)
    return JsonResponse(consi_infoo)


# views.py
from django.views.generic import TemplateView

# class ReportView(TemplateView):
#     obj = Delivery_Run.objects.all()
#     template_name = 'delivery_report.html'

#     def get_context_data(self, **kwargs):
#         obj = Delivery_Run.objects.all()
#         # Define the data you want to include in your report
#         data = {'name': 'John Doe', 'age': 30, 'occupation': 'Software Developer','obj':obj}
#         # Add the data to the context dictionary
        
#         # context = super().get_context_data(**kwargs)
#         delivery_runs = Delivery_Run.objects.all()

#         # Add the data to the context dictionary
#         context = super().get_context_data(**kwargs)
#         context['delivery_runs'] = delivery_runs

#         context['data'] = data
#         return context
    
  
# class ReportView(TemplateView):
#     obj = Delivery_Run.objects.all()
#     template_name = 'delivery_report.html'

#     def get_context_data(self, **kwargs):
#         obj = Delivery_Run.objects.all()
#         # Define the data you want to include in your report
#         data = {'name': 'John Doe', 'age': 30, 'occupation': 'Software Developer','obj':obj}
#         # Add the data to the context dictionary
        
#         # context = super().get_context_data(**kwargs)
#         delivery_runs = Delivery_Run.objects.all()

#         # Add the data to the context dictionary
#         context = super().get_context_data(**kwargs)
#         context['delivery_runs'] = delivery_runs

#         context['data'] = data
        
    
#     html = template_name.render(context)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="Delivery_Run.pdf"'
#     # create a pdf object
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     # if error then show some funy view
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response



# from django.views.generic import TemplateView
# from django.template.loader import get_template
# from django.http import HttpResponse


# class ReportView(TemplateView):
#     template_name = 'delivery_report.html'

#     def get_context_data(self, **kwargs):
#         # Get the data you want to include in your report
#         delivery_runs = Delivery_Run.objects.all()
#         data = {'name': 'John Doe', 'age': 30, 'occupation': 'Software Developer', 'delivery_runs': delivery_runs}

#         # Add the data to the context dictionary
#         context = super().get_context_data(**kwargs)
#         context['data'] = data
#         return context

#     def get(self, request, *args, **kwargs):
#         # Render the template as HTML
#         template = get_template(self.template_name)
#         html = template.render(self.get_context_data())

#         # Generate a PDF file
#         pdf_file = generate_pdf(html)

#         # Return the PDF as a response
#         response = HttpResponse(pdf_file, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="Delivery_Run.pdf"'
#         return response

        
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa


# class ReportView(TemplateView):
#     template_name = 'delivery_report.html'

#     def get_context_data(self, **kwargs):
#         # Get the data you want to include in your report
#         delivery_runs = Delivery_Run.objects.all()
#         data = {'name': 'John Doe', 'age': 30, 'occupation': 'Software Developer', 'delivery_runs': delivery_runs}

#         # Add the data to the context dictionary
#         context = super().get_context_data(**kwargs)
#         context['data'] = data

#         return context

#     def get(self, request, *args, **kwargs):
#         # Render the template with the data
#         template = get_template(self.template_name)
#         html = template.render(self.get_context_data())

#         # Create a PDF object
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="Delivery_Run.pdf"'
#         pdf_file = BytesIO()

#         # Generate the PDF using Pisa
#         pisa_status = pisa.CreatePDF(html, dest=pdf_file)

#         # If there was an error, return an error response
#         if pisa_status.err:
#             return HttpResponse('We had some errors <pre>' + html + '</pre>')

#         # Otherwise, return the PDF as the response
#         pdf = pdf_file.getvalue()
#         response.write(pdf)
#         pdf_file.close()
#         return response


# class ReportView(TemplateView):
#     template_name = 'delivery_report.html'

#     def get_context_data(self, **kwargs):
#         # Get the data you want to include in your report
#         delivery_runs = Delivery_Run.objects.all()
#         data = {'name': 'John Doe', 'age': 30, 'occupation': 'Software Developer', 'delivery_runs': delivery_runs}

#         # Add the data to the context dictionary
#         context = super().get_context_data(**kwargs)
#         context['data'] = data

#         return context

#     def get(self, request, *args, **kwargs):
#         # Get the data and render the template with the data
#         delivery_runs = Delivery_Run.objects.all()
#         data = {'name': 'John Doe', 'age': 30, 'occupation': 'Software Developer', 'delivery_runs': delivery_runs}
#         template = get_template(self.template_name)
#         html = template.render({'data': data})

#         # Create a PDF object
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="Delivery_Run.pdf"'
#         pdf_file = BytesIO()

#         # Generate the PDF using Pisa
#         pisa_status = pisa.CreatePDF(html, dest=pdf_file)

#         # If there was an error, return an error response
#         if pisa_status.err:
#             return HttpResponse('We had some errors <pre>' + html + '</pre>')

#         # Otherwise, return the PDF as the response
#         pdf = pdf_file.getvalue()
#         response.write(pdf)
#         pdf_file.close()
#         return response

# pdf code final
# def ReportView(request):
#     template = get_template('delivery_report.html')
#     delivery_runs = Delivery_Run.objects.all()
#     context = {
#         'delivery_runs':delivery_runs,
               
#                }
#     html = template.render(context)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="Delivery_Run.pdf"'
#     # create a pdf object
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     # if error then show some funy view
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

# search branchwise

from django.db.models import Q

def Branch_ReportView(request):
    template = get_template('delivery_report.html')
    delivery_runs = Delivery_Run.objects.all()
    branch_query = request.GET.get('branch')

    if branch_query:
        delivery_runs = delivery_runs.filter(Q(s_Branch__icontains=branch_query))

    context = {
        'delivery_runs':delivery_runs,
    }
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Delivery_Run.pdf"'
    # create a pdf object
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response 

def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        title = request.POST['title']
        new_image = Image(title=title, image=image)
        new_image.save()
    return render(request, 'upload.html')

def display_image(request):
    images = Image.objects.all()
    return render(request, 'display.html', {'images': images})


def ReportView(request):
    template = get_template('delivery_report.html')
    delivery_runs = Delivery_Run.objects.all()
    
    logo = Image.objects.all()

    # get the search query parameters
    branch = request.GET.get('branch')
    from_query = request.GET.get('from')
    to_query = request.GET.get('to')

    # filter the data based on search querie
    print("hie")
    print("hiiiiiiiiii" ,branch)
    if branch:
        delivery_runs = Delivery_Run.objects.filter(s_Branch=branch)
    


    if from_query:
        delivery_runs = delivery_runs.filter(s_From=from_query)
    if to_query:
        delivery_runs = delivery_runs.filter(s_To=to_query)

    context = {
        'delivery_runs': delivery_runs,
        'logo': logo,
    }
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Delivery_Run.pdf"'
    # create a pdf object
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# code for branch report

# def Branch_ReportView(request):
#     template = get_template('delivery_report.html')
#     delivery_runs = Delivery_Run.objects.all()

#     # get the search query parameters
#     branch_query = request.GET.get('branch')
   

#     # filter the data based on search queries
#     if branch_query:
#         delivery_runs = Delivery_Run.objects.filter(s_Branch=branch_query)



#     context = {
#         'delivery_runs': delivery_runs,
#     }
#     html = template.render(context)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="Delivery_Run.pdf"'
#     # create a pdf object
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     # if error then show some funy view
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

