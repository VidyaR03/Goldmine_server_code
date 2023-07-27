from goldmineApp . models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required


# @login_required(login_url='admin_login_url')
def fn_Operations_View(request):
    pickups = Pickup_Request.objects.all().count()
    consignments = Consignment_No.objects.all().count()
    pickuprunsheets = Pickup_Runsheet.objects.all().count()
    tripsheets = Trip_Sheet.objects.all().count()
    manifest = Manifest_Load.objects.all().count()
    context = {
        'pickups':pickups,
        'consignments':consignments,
        'manifest':manifest,
        'pickuprunsheets':pickuprunsheets,
        'tripsheets':tripsheets
    }
    return render(request,'Operations/operations.html',context)
