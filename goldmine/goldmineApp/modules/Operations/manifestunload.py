from goldmineApp . models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Max,Min,Avg,Sum,Count
from django.core.paginator import Paginator
import datetime
from django.db.models import Q
from django.urls import reverse


# @login_required(login_url='admin_login_url')
def fn_Manifest_Unload_List_View(request):
    if request.method =="POST":
        fromdate= request.POST.get("from_date")
        todate= request.POST.get("to_date")
        result = Manifest_UnLoad.objects.all().filter(s_Date__range=(fromdate, todate)) 
        return render(request,'manifest_unload_list.html',{'data':result})
    else :
        form = Manifest_UnLoad.objects.filter(s_Status=False)
        paginator = Paginator(form,10)
        page_number = request.GET.get('page')
        form4 = paginator.get_page(page_number)
        context = {'form':form,'form4':form4}
    return render(request,'manifest_unload_list.html',context)


def fn_Manifest_unload_List_of_Consignment_View(request):
    '''
      this view function is for list all Consignmnet with checkbox.
    '''
    form = Consignment_No.objects.all()
    form1 =  Branch.objects.all()
    form5 = Vehicle.objects.all()
    datex = datetime.date.today()
    context = {'form':form,'form1':form1,'form5':form5,'datex':datex}
    if request.method == 'POST':
       
        i_Manifest_Unload_No = 6001 if Manifest_UnLoad.objects.count() == 0 else Manifest_UnLoad.objects.aggregate(max=Max('i_Manifest_Unload_No'))["max"]+1

        s_vehicle_number = Vehicle.objects.filter(s_vehicle_number=request.POST.get('vehicle_number')).first()
     
        s_Date = request.POST.get('date')
        s_Branch = request.POST.get('branch_city')
        num = str(i_Manifest_Unload_No)
        g = str(s_Branch)
        s = g[0:3]
        i_MR_NO = s.upper() + '_' + num

        # pr = request.POST.getlist('prid')
        # i_PR_NO = ''
        # for i in pr:
        #     i_PR_NO += str(i) + ',' 
        # print(i_PR_NO)     

        obj = Manifest_UnLoad(
            s_Date=s_Date,
            i_Manifest_Unload_No=i_Manifest_Unload_No,
            s_vehicle_number=s_vehicle_number,
            s_Branch=s_Branch,
            i_MR_NO = i_MR_NO,
            )
        obj.save()
        id = Manifest_UnLoad.objects.get(i_Manifest_Unload_No=i_Manifest_Unload_No).id
        print(id)
        manifest_unload = Manifest_UnLoad.objects.get(id=id)
        value = request.POST.getlist('mrid')
        for val in value:
            obj = Consignment_No.objects.get(id=val)
            obj.i_Manifest_Unload_No = manifest_unload
            obj.s_Status = True

            obj.save()

        # Manifest_UnLoad.objects.filter(id=id).update(
        #     i_Mani_NO=i_Mani_NO
        # )
        return redirect('manifest_unload_list_url')

    return render(request,'add_manifest_unload.html',context)



# @login_required(login_url='admin_login_url')
def fn_Add_Manifest_Unload_View(request):
    form = Manifest_UnLoad.objects.filter(s_Status=1)
    cn_no = Consignment_No.objects.filter(m_status=0)
    mani = Manifest_Load.objects.all()
    branch = Branch.objects.all()
    i_Manifest_Unload_No = 6001 if Manifest_UnLoad.objects.count() == 0 else Manifest_UnLoad.objects.aggregate(max=Max('i_Manifest_Unload_No'))["max"]+1
    context = {
        'form':form,
        'cn_no':cn_no,
        'branch':branch,
        'mani':mani,
        'i_Manifest_Unload_No':i_Manifest_Unload_No,
        }
    if request.method == 'POST':
        m_no = request.POST.getlist("select_list[]")
        mr_len = len(m_no)
        if mr_len <=1 :
            for i in m_no:
                mr_no = i
        else:
            for i in m_no:
                mr_no = ','.join(m_no)

        obj = Manifest_UnLoad(
            i_Manifest_Unload_No = int(request.POST.get('manifest_upload_no')),
            s_Date = request.POST.get('unload_date'),
            s_Branch = request.POST.get('branch_city'),
            i_MR_NO = mr_no,
            s_Manifest_No = request.POST.get('manifest_no')
            )
        obj.save()
       
        value = request.POST.getlist('select_list[]')
        for val in value:
            obj = Consignment_No.objects.get(i_LR_NO=val)
            new_obj = Consignment_No.objects.get(i_LR_NO=val, i_Mani_NO=obj.i_Mani_NO)
            new_obj.i_Mani_Un_NO = i_Manifest_Unload_No
            new_obj.m_status = True
            new_obj.save()
       
        return redirect('manifest_unload_list_url')
    
    return render(request,'add_manifest_unload.html',context)

# @login_required(login_url='admin_login_url')
def fn_Manifest_Unload_Details_View(request,id):
    manifest = Manifest_UnLoad.objects.get(id=id)
    m_id =  manifest.i_Manifest_Unload_No
    form = Consignment_No.objects.filter(i_Mani_Un_NO=m_id)
    date = datetime.date.today()
    context = {
        'manifest':manifest,
        'form':form,
        'date':date
    }
    
    return render(request,'manifest-unload-preview.html',context)



# @login_required(login_url='admin_login_url') 
def fn_Manifest_Unload_Update_View(request,id):

    obj = Manifest_UnLoad.objects.get(id=id)
    m_id =  obj.i_Manifest_Unload_No
    obj2 = Consignment_No.objects.filter(i_Mani_Un_NO = m_id)
    form = Consignment_No.objects.filter(m_status=1)
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
                i_Mani_Un_NO = None,
                m_status = False
            )
        i_Manifest_Unload_No =request.POST.get('manifest_unloadno')
        s_Date=request.POST.get('current_date')
        s_Branch = request.POST.get('branch_city')

        m = Manifest_UnLoad(
            id=id,
            i_Manifest_Unload_No=i_Manifest_Unload_No,
            s_Date=s_Date, 
            s_Branch=s_Branch,
            s_Manifest_No=obj.s_Manifest_No,
            )
        m.save()

        manifest = Manifest_UnLoad.objects.get(id=id)
        
        value = request.POST.getlist('consignments')
        for val in value:
            obj = Consignment_No.objects.get(id=val)
            obj.m_status = True
            obj.save()

        return redirect('manifest_unload_list_url')    

    return render(request,'manifest_unload_update.html', context)




# @login_required(login_url='admin_login_url')
def fn_Manifest_Unload_Delete_View(request,id):
    obj = Manifest_UnLoad.objects.get(id=id)
    obj.s_Status = 0
    obj.save()
    return redirect('manifest_unload_list_url')
