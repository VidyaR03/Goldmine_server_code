from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from goldmineApp . models import *
from goldmineApp. models import *
import json
from django.db.models import Q



# def fn_Dashboard_View(request):
#     form = Invoice.objects.order_by('-s_Bill_Date')[:5]
#     data = Consignment_No.objects.order_by('-i_No_of_Articles')[:5]
#     manifest_load = Manifest_Load.objects.all().count()
#     manifest_unload = Manifest_UnLoad.objects.all().count()
#     pune = Pickup_Request.objects.filter(s_From = "Pune").count()
#     mumbai = Pickup_Request.objects.filter(s_From = "Mumbai").count()


#     context = {'form':form,
#                'data':data,
#                'manifest_load':manifest_load,
#                'manifest_unload':manifest_unload,
#                'pune':pune,
#                'mumbai':mumbai
#                }  



#     return render(request,'index.html',context)



def fn_Dashboard_View(request):
    # ...

    # Prepare data for the chart
    form = Invoice.objects.order_by('-s_Bill_Date')[:5]
    data = Consignment_No.objects.order_by('-i_No_of_Articles')[:5]
    manifest_load = Manifest_Load.objects.all().count()
    manifest_unload = Manifest_UnLoad.objects.all().count()
    pune = Pickup_Request.objects.filter(s_From = "Pune").count()
    mumbai = Pickup_Request.objects.filter(s_From = "Mumbai").count()
    kolkata = Pickup_Request.objects.filter(s_From = "Kolkata").count()
    patna = Pickup_Request.objects.filter(s_From = "Patna").count()
    hydrabad = Pickup_Request.objects.filter(s_From = "Hydrabad").count()
    bangalore = Pickup_Request.objects.filter(s_From = "Bangalore").count()
    delhi = Pickup_Request.objects.filter(Q(s_From="Delhi") | Q(s_From="New Delhi")).count()
    chandigarh = Pickup_Request.objects.filter(s_From = "Chandigarh").count()


    pickup_request = Pickup_Request.objects.all().count()
    consignment_request = Consignment_No.objects.all().count
    cpune = Consignment_No.objects.filter(s_From = "Pune").count()
    cmumbai = Consignment_No.objects.filter(s_From = "Mumbai").count()
    ckolkata = Consignment_No.objects.filter(s_From = "Kolkata").count()
    cpatna = Consignment_No.objects.filter(s_From = "Patna").count()
    chydrabad = Consignment_No.objects.filter(s_From = "Hydrabad").count()
    cbangalore = Consignment_No.objects.filter(s_From = "Bangalore").count()
    rpune = Pickup_Runsheet.objects.filter(s_Branch = "Pune").count()
    rmumbai = Pickup_Runsheet.objects.filter(s_Branch = "Mumbai").count()
    cdelhi = Consignment_No.objects.filter(Q(s_From="Delhi") | Q(s_From="New Delhi")).count()
    cchandigarh = Consignment_No.objects.filter(s_From = "Chandigarh").count()

    
    
    chart_data = {
        'labels': ['Pune', 'Mumbai'],
        'data': [
            { 'x': 0, 'y': rpune },
            { 'x': 0, 'y': rmumbai }
        ],
        'color': '#7579ff'
    }


    # chart_data = {
    #     'labels': ['Pune', 'Mumbai'],
    #     'data': [pune, mumbai],
    #     'colors': ['#7579ff', '#3cba92']
    # }

    context = {
        # ...
        'form':form,
        'data':data,
        'manifest_load':manifest_load,
        'manifest_unload':manifest_unload,      
        'chart_data': json.dumps(chart_data),  # Convert the chart data to JSON,
        'pickup_request':pickup_request,
        'consignment_request':consignment_request,
        'pune':pune,
        'chandigarh':chandigarh,
        'mumbai':mumbai,
        'kolkata':kolkata,
        'patna':patna,
        'hydrabad':hydrabad,
        'bangalore':bangalore,
        'delhi':delhi,
        'cpune':cpune,
        'cdelhi':cdelhi,
        'cchandigarh':cchandigarh,
        'cmumbai':cmumbai,
        'ckolkata':ckolkata,
        'cpatna':cpatna,
        'chydrabad':chydrabad,
        'cbangalore':cbangalore,
        'rpune':rpune,
        'rmumbai':rmumbai

    }


    return render(request, 'index.html', context)


