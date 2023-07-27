from goldmineApp. models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Max
import datetime
from django.core.paginator import Paginator


def fn_Pickup_Runsheet_List_View(request):
    '''
    This view function for display all Pickup Runsheet with pickup data data.
    '''
    if request.method =="POST":
        fromdate= request.POST.get("from_date")
        todate= request.POST.get("to_date")
        result = Pickup_Runsheet.objects.all().filter(s_Date__range=(fromdate, todate)) 
        return render(request,'pickup_runsheet_list.html',{'data':result})
    else :
        form = Pickup_Runsheet.objects.all()
        paginator = Paginator(form,10)
        page_number = request.GET.get('page')
        form4 = paginator.get_page(page_number)
        context = {'form':form,'form4':form4}
        return render(request,'pickup_runsheet_list.html',context)

def fn_Pickup_Runsheet_Add_View(request):
    '''
    This view function for add new pickup runsheet.
    '''  
    form1 = Consignment_No.objects.all()  
    form = Vehicle.objects.all()
    form3 = Pickup_Request.objects.all()
    datex = datetime.date.today()
    context = {'form':form,'form1':form1,'form3':form3,'datex':datex}
    if request.method == 'POST':
        s_Date = request.POST.get('s_date')
        s_vehicle_number = Vehicle.objects.filter(s_vehicle_number=request.POST.get('vehicle_number')).first()
     
        obj = Pickup_Runsheet(
            s_Date=s_Date,
            s_vehicle_number=s_vehicle_number,
            )
        obj.save()
        return redirect('pickup_runsheet_list_view')

    return render(request,'add-pickup-runsheet.html',context)


def fn_Pickup_Runsheet_List_of_Pickup_request_View(request):
    '''
      this view function is for list all pickup request with checkbox.
    '''
    form = Consignment_No.objects.all()
    form1 =  Branch.objects.all()
    form5 = Vehicle.objects.all()
    datex = datetime.date.today()
    context = {'form':form,'form1':form1,'form5':form5,'datex':datex}
    if request.method == 'POST':
       
        i_Pickup_Runsheet_No = 3001 if Pickup_Runsheet.objects.count() == 0 else Pickup_Runsheet.objects.aggregate(max=Max('i_Pickup_Runsheet_No'))["max"]+1

        s_vehicle_number = Vehicle.objects.filter(s_vehicle_number=request.POST.get('vehicle_number')).first()
     
        s_Date = request.POST.get('date')
        s_Branch = request.POST.get('branch_city')
        num = str(i_Pickup_Runsheet_No)
        g = str(s_Branch)
        s = g[0:3]
        i_PR_NO = s.upper() + '_' + num

        # pr = request.POST.getlist('prid')
        # i_PR_NO = ''
        # for i in pr:
        #     i_PR_NO += str(i) + ',' 
        # print(i_PR_NO)     

        obj = Pickup_Runsheet(
            s_Date=s_Date,
            i_Pickup_Runsheet_No=i_Pickup_Runsheet_No,
            s_vehicle_number=s_vehicle_number,
            s_Branch=s_Branch,
            i_PR_NO = i_PR_NO,
            )
        obj.save()
        id = Pickup_Runsheet.objects.get(i_Pickup_Runsheet_No=i_Pickup_Runsheet_No).id
        print(id)
        pickup_runsheet = Pickup_Runsheet.objects.get(id=id)
        value = request.POST.getlist('prid')
        for val in value:
            obj = Consignment_No.objects.get(id=val)
            obj.i_Pickup_Runsheet = pickup_runsheet
            obj.s_Status = True

            obj.save()

        Pickup_Runsheet.objects.filter(id=id).update(
            s_vehicle_number=s_vehicle_number
        )
        return redirect('pickup_runsheet_list_url')

    return render(request,'add-pickup-runsheet.html',context)


def fn_Pickup_Runsheet_Delete_View(request,id):
    '''
    This view function for delete the specific Pickup Request.
    '''
    obj = Pickup_Runsheet.objects.get(id=id)
    obj.delete()
    return redirect('pickup_runsheet_list_url')

# def fn_Pickup_Runsheet_Details_View(request,id):
#     obj = Pickup_Runsheet.objects.get(id=id)
#     pr = obj.i_PR_NO.split(',')
#     list = []
#     for i in range(len(pr)-1):
#         data = Pickup_Request.objects.filter(i_PR_NO = (pr[i])).first()
#         list.append(data)
    
#     context = {
#         'obj':obj,
#         'pr_no':pr,
#         'list' : list
    
#         }
#     return render(request,'pickup_runsheet_preview.html',context)

    
# PDF GENERATE CODE 

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_pdf(request):
    template = get_template('Operations/Pickup_Runsheet/pdff.html')
   
    context = {'my_variable': 'Hello World!'}
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Pickup_Runsheet.pdf"'
    # create a pdf object
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def fn_Pickup_Runsheet_Details_View(request,id):
    pickup_runsheet = Pickup_Runsheet.objects.get(id=id)
    form = Consignment_No.objects.filter(i_Pickup_Runsheet=id)
    
    
    
    context = {
        'pickup_runsheet':pickup_runsheet,
        'form':form,
        
    }
    
    return render(request,'pickup_runsheet_preview.html',context)





def fn_Pickup_Runsheet_Update_View(request,id):
    obj = Pickup_Runsheet.objects.get(id=id)
    form = Vehicle.objects.all()
    form1 =  Branch.objects.all()

    obj2 = Consignment_No.objects.filter(i_Pickup_Runsheet=id)
    form2 = Consignment_No.objects.filter(s_Status=0)

    s_Date = datetime.date.today()
    context = {'form':form,'form2':form2,'obj':obj ,'obj2':obj2,'s_Date':s_Date,'form1':form1}
    
    
    if request.method == 'POST':
        for x in form2:
            Consignment_No.objects.filter(id=x.id).update(
                i_Pickup_Runsheet=None,
                s_Status = False
            )

        s_Date = request.POST.get('date')
        s_vehicle_number = Vehicle.objects.filter(s_vehicle_number=request.POST.get('vehicle_number')).first()
        i_PR_NO = request.POST.get('i_PR_NO')
        s_Branch = request.POST.get('branch_city')
        i_Pickup_Runsheet_No=obj.i_Pickup_Runsheet_No


     
        p = Pickup_Runsheet(
            id=id,
            s_Date=s_Date,
            s_vehicle_number=s_vehicle_number,
            i_PR_NO=i_PR_NO,
            s_Branch=s_Branch,
            i_Pickup_Runsheet_No=i_Pickup_Runsheet_No

            )
        p.save()

        pickup_runsheet = Pickup_Runsheet.objects.get(id=id)

        value = request.POST.getlist('prid')

        for val in value:
            obj=Consignment_No.objects.get(id=val)
            obj.i_Pickup_Runsheet =pickup_runsheet
            obj.s_Status = True

            obj.save()
        Pickup_Runsheet.objects.filter(id=id).update(
            s_vehicle_number=s_vehicle_number
        )


        return redirect('pickup_runsheet_list_url')
    return render(request,'edit_pickup_runsheet.html',context)

    


    
    
# def fn_Pickup_Runsheet_Deatails_View(request):

#     vehid = request.GET.get('vehid')

#     vehicle_number = Pickup_Runsheet.objects.filter(id=int(vehid)).first()
#     slt = vehicle_number.slts.through.objects.filter(Vehicle_id=vehicle_number.id)

#     queryset_list = []
#     for i in slt:
#         data = []
#         queryset = Pickup_Request.objects.filter(id__icontains=i.cl_slt_id).first()
#         data.append({

#             'id': queryset.id,

#             'ch_name': queryset.ch_name,

#             'ch_priority': queryset.ch_priority,

#             'ch_request_type': queryset.ch_request_type,

#             'ch_metric': queryset.ch_metric,

#             'ch_value': queryset.ch_value,

#             'ch_unit': queryset.ch_unit

#         })
#         queryset_list.append(data)




#     json_data = json.dumps(queryset_list)

#     return HttpResponse(json_data, content_type='application/json')


    
   
def addrunsheet(request):
    if request.method == "POST":
        list_id = request.POST.getlist('id[]')
        vech_id = request.POST.get('v')
        vech = Vehicle.objects.filter(id=vech_id).first()
  
        for i in list_id:
            vl = Pickup_Runsheet.objects.filter(id=i).first()
            vl.save()
    return redirect('pickup_runsheet_list_url',{'vech':vech})
# def fn_search_pickuprunsheet_by_branch(request, branch):
#     """

#     Args:
#         request (_type_): _description_
#         branch (_type_): _description_
#     """
#     if request.method == 'GET':
        
#         branch = request.GET.get(branch)
        
# def check_mychecklist(request):
#     if request.method =='POST':
#         check =request.post.getlist('check[]')
#         for i in check :
#             
        