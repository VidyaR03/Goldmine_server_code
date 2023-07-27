from goldmineApp . models import *
from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator
from django.http import JsonResponse
import datetime
from django.db.models import Max





def fn_listing_voucher_list_view(request):
    if request.method == "POST":
        fromdate = request.POST.get("from_date")
        todate = request.POST.get("to_date")
        result = add_voucher.objects.all().filter(d_voucher_date__range=(fromdate, todate))
        context = {'data' : result}
        return render(request,'finance/listing_voucher/details.html', context)
    else:
        voucher = add_voucher.objects.all()
        paginator = Paginator(voucher, 10)
        page_number = request.GET.get('page')
        form4 = paginator.get_page(page_number)
        context = {'voucher' : voucher,'form4':form4}
    return render(request,'finance/listing_voucher/details.html', context)

# @login_required(login_url='admin_login_url')
# def fn_listing_voucher_Delete_View(request,id):
#     '''
#     This view function for delete the specifice add_voucher.
#     '''
#     obj = add_voucher.objects.get(id=id)
#     obj.delete()
#     return redirect('listing_voucher_list_url')
