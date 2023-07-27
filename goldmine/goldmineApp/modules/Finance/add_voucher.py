from goldmineApp . models import *
from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator
from django.http import JsonResponse
import datetime
from django.db.models import Max


from django.shortcuts import render, redirect
from django.db.models import Max
# from .models import add_voucher

# def fn_add_voucher_add_view(request):
#     branch = Branch.objects.all()

#     context = {
#         'branch': branch,
#     }

#     if request.method == 'POST':
#         s_voucher_type = request.POST.get('s_voucher_type')
#         prefix = ''

#         if s_voucher_type == 'Receipts':
#             prefix = 'Receipts'
#         elif s_voucher_type == 'Payments':
#             prefix = 'Payments'
#         elif s_voucher_type == 'Credit':
#             prefix = 'Credit'
#         else:
#             prefix = 'Unknown'

#         max_voucher_number = add_voucher.objects.filter(s_voucher_type=s_voucher_type).aggregate(max=Max('i_Vid_No'))['max']
#         i_Vid_No = 1 if max_voucher_number is None else max_voucher_number + 1

#         i_VR_NO = f'{prefix}{i_Vid_No}'

#         s_branch = Branch.objects.filter(s_Branch_City=request.POST.get('branch_city')).first()
#         d_voucher_date = request.POST.get('d_voucher_date')
#         by_or_to = request.POST.get('by_or_to')
#         s_perticular = request.POST.getlist('s_perticular')  # Get a list of perticulars
#         s_debit = request.POST.getlist('s_debit')  # Get a list of debits
#         s_credit = request.POST.getlist('s_credit')  # Get a list of credits

#         s_total_debit = sum([float(debit) for debit in int(s_debit)])  # Calculate total debit
#         s_total_credit = sum([float(credit) for credit in int(s_credit)])  # Calculate total credit

#         obj = add_voucher(
#             s_branch=s_branch,
#             i_Vid_No=i_Vid_No,
#             i_VR_NO=i_VR_NO,
#             d_voucher_date=d_voucher_date,
#             s_voucher_type=s_voucher_type,
#             by_or_to=by_or_to,
#             s_total_debit=s_total_debit,
#             s_total_credit=s_total_credit,
#         )

#         obj.save()

#     # Save multiple perticulars with their corresponding debit and credit values
#         for i in range(len(s_perticular)):
#             perticular = s_perticular[i]
#             debit = s_debit[i]
#             credit = s_credit[i]

#             voucher_entry = VoucherEntry(
#                 add_voucher=obj,
#                 s_perticular=perticular,
#                 s_debit=debit,
#                 s_credit=credit,
#             )

#         voucher_entry.save()
#         return redirect('add_voucher_list_url')
#     return render(request, 'finance/voucher/add.html', context)


# def fn_add_voucher_add_view(request):
#     branch = Branch.objects.all()

#     context = {
#         'branch': branch,
#     }

#     if request.method == 'POST':
#         s_voucher_type = request.POST.get('s_voucher_type')
#         prefix = ''

#         if s_voucher_type == 'Receipts':
#             prefix = 'Receipts_'
#         elif s_voucher_type == 'Payments':
#             prefix = 'Payments_'
#         elif s_voucher_type == 'Credit Note':
#             prefix = 'Credit Note_'
#         else:
#             prefix = 'Unknown'

#         max_voucher_number = add_voucher.objects.filter(s_voucher_type=s_voucher_type).aggregate(max=Max('i_Vid_No'))['max']
#         i_Vid_No = 1 if max_voucher_number is None else max_voucher_number + 1
#         i_VR_NO = f'{prefix}{i_Vid_No}'
#         s_branch = Branch.objects.filter(s_Branch_City=request.POST.get('branch_city')).first()
#         d_voucher_date = request.POST.get('d_voucher_date')
#         by_or_to = request.POST.get('by_or_to')
#         # s_perticular = request.POST.get('s_perticular[]')
#         s_debit = request.POST.get('s_debit[]')
#         s_credit = request.POST.get('s_credit[]')
#         s_total_debit = request.POST.get('s_total_debit')
#         s_total_credit = request.POST.get('s_total_credit')

#         tm = request.POST.getlist('s_perticular[]')
#         s_perticular = ''
#         for i in tm:
#              s_perticular += str(i) + ',' 

#         debit = request.POST.getlist('s_debit[]')
#         s_debit = ''
#         for i in debit:
#              s_debit += str(i) + ',' 
        
#         credit = request.POST.getlist('s_credit[]')
#         s_credit = ''
#         for i in credit:
#              s_credit += str(i) + ',' 
    

#         obj = add_voucher(
#             s_branch=s_branch,
#             i_Vid_No=i_Vid_No,
#             i_VR_NO=i_VR_NO,
#             d_voucher_date=d_voucher_date,
#             s_voucher_type=s_voucher_type,
#             by_or_to=by_or_to,
#             s_perticular=s_perticular,
#             s_debit=s_debit,
#             s_credit=s_credit,
#             s_total_debit=s_total_debit,
#             s_total_credit=s_total_credit,
#         )

#         obj.save()
#         return redirect('add_voucher_list_url')

#     return render(request, 'finance/voucher/add.html', context)


def fn_add_voucher_add_view(request):
    branch = Branch.objects.all()

    context = {
        'branch': branch,
    }
    if request.method == 'POST':
        s_voucher_type = request.POST.get('s_voucher_type')
        prefix = ''
        if s_voucher_type == 'Receipts':
            prefix = 'Receipts'
        elif s_voucher_type == 'Payments':
            prefix = 'Payments'
        elif s_voucher_type == 'Credit':
            prefix = 'Credit'
        else:
            prefix = 'Unknown'

        max_voucher_number = add_voucher.objects.filter(s_voucher_type=s_voucher_type).aggregate(max=Max('i_Vid_No'))['max']
        i_Vid_No = 1 if max_voucher_number is None else max_voucher_number + 1

        i_VR_NO = f'{prefix}{i_Vid_No}'

        s_branch = Branch.objects.filter(s_Branch_City=request.POST.get('branch_city')).first()
        d_voucher_date = request.POST.get('d_voucher_date')
        by_or_to = request.POST.get('by_or_to')
        s_perticular = request.POST.getlist('s_perticular')
        s_debit = request.POST.getlist('s_debit')
        s_credit = request.POST.getlist('s_credit')

        if len(s_perticular) == 1:
            s_total_debit = s_debit[0]
            s_total_credit = s_credit[0]
        else:
            s_total_debit = sum([float(debit) for debit in s_debit])
            s_total_credit = sum([float(credit) for credit in s_credit])

        obj = add_voucher(
            s_branch=s_branch,
            i_Vid_No=i_Vid_No,
            i_VR_NO=i_VR_NO,
            d_voucher_date=d_voucher_date,
            s_voucher_type=s_voucher_type,
            by_or_to=by_or_to,
            s_perticular=s_perticular,
            s_debit=s_debit,
            s_credit=s_credit,
            s_total_debit=s_total_debit,
            s_total_credit=s_total_credit,
        )
        obj.save()
        return redirect('add_voucher_list_url')
    return render(request, 'finance/voucher/add.html', context)




# def fn_add_voucher_add_view(request):
#     branch = Branch.objects.all()
#     context = {
#         'branch' : branch, 
#     }

#     if request.method == 'POST':
#         # Get the selected voucher type
#         s_voucher_type = request.POST.get('s_voucher_type')
#         # Determine the prefix based on the voucher type
#         if s_voucher_type == 'Receipts':
#             prefix = 'Receipts'
#         elif s_voucher_type == 'Payments':
#             prefix = 'Payments'
#         elif s_voucher_type == 'Credit Note':
#             prefix = 'Credit'
#         else:
#             prefix = 'Unknown'

#         max_voucher_number = add_voucher.objects.filter(s_voucher_type=s_voucher_type).aggregate(max=Max('i_Vid_No'))['max']
#         if max_voucher_number is None:
#             i_Vid_No = 1
#         else:
#             i_Vid_No = max_voucher_number + 1
#             # Generate the voucher ID
#         i_VR_NO = f'{prefix}{i_Vid_No}'  # Set a default prefix if needed
#         # Determine the maximum voucher number for the selected voucher type
#         # max_voucher_number = add_voucher.objects.filter(s_voucher_type=s_voucher_type).aggregate(max=Max('i_Vid_No'))['max']
#         # # i_Vid_No = 1 if max_voucher_number is None else max_voucher_number + 1
#         # i_Vid_No = 1 if add_voucher.objects.count() == 0 else add_voucher.objects.aggregate(max=Max('i_Vid_No'))["max"] + 1

#         # # Generate the voucher ID
#         # i_VR_NO = f'{prefix}{i_Vid_No}' 
    
#         # i_Vid_No = 1 if add_voucher.objects.count() == 0 else add_voucher.objects.aggregate(max=Max('i_Vid_No'))["max"]+1
#         # s_voucher_type = request.POST.get('s_voucher_type')
#         # i_VR_NO = str(i_Vid_No)  
#         # v_type = str(s_voucher_type)
#         # type = v_type[0:7]
#         # voucher_id =type.upper() + '_' + i_VR_NO           
#         s_branch = Branch.objects.filter(s_Branch_City = request.POST.get('branch_city')).first()
#         d_voucher_date = request.POST.get('d_voucher_date')
#         by_or_to = request.POST.get('by_or_to')
#         s_perticular = request.POST.get('s_perticular')
#         s_debit = request.POST.get('s_debit')
#         s_credit = request.POST.get('s_credit')
#         s_total_debit = request.POST.get('s_total_debit')
#         s_total_credit = request.POST.get('s_total_credit')

#         obj = add_voucher(
#             s_branch = s_branch,
#             # i_Vid_No = i_Vid_No,
#             i_VR_NO = i_VR_NO,
#             d_voucher_date = d_voucher_date,
#             s_voucher_type = s_voucher_type,
#             by_or_to = by_or_to,
#             s_perticular = s_perticular,
#             s_debit = s_debit,
#             s_credit = s_credit,
#             s_total_debit = s_total_debit,
#             s_total_credit = s_total_credit,
#         )

#         obj.save()
#         return redirect('add_voucher_list_url')
#     return render(request,'finance/voucher/add.html', context)



# def fn_add_voucher_add_view(request):
#     branch = Branch.objects.all()

#     context = {
#         'branch' : branch, 
#     }

#     if request.method == 'POST':
#         i_Vid_No = 1 if add_voucher.objects.count() == 0 else add_voucher.objects.aggregate(max=Max('i_Vid_No'))["max"]+1
#         s_voucher_type = request.POST.get('s_voucher_type')
#         i_VR_NO = str(i_Vid_No)  
#         v_type = str(s_voucher_type)
#         type = v_type[0:7]
#         voucher_id =type.upper() + '_' + i_VR_NO           
#         s_branch = Branch.objects.filter(s_Branch_City = request.POST.get('branch_city')).first()
#         d_voucher_date = request.POST.get('d_voucher_date')
#         by_or_to = request.POST.get('by_or_to')
#         s_perticular = request.POST.get('s_perticular')
#         s_debit = request.POST.get('s_debit')
#         s_credit = request.POST.get('s_credit')
#         s_total_debit = request.POST.get('s_total_debit')
#         s_total_credit = request.POST.get('s_total_credit')

#         obj = add_voucher(
#             s_branch = s_branch,
#             i_Vid_No = i_Vid_No,
#             i_VR_NO = voucher_id,
#             d_voucher_date = d_voucher_date,
#             s_voucher_type = s_voucher_type,
#             by_or_to = by_or_to,
#             s_perticular = s_perticular,
#             s_debit = s_debit,
#             s_credit = s_credit,
#             s_total_debit = s_total_debit,
#             s_total_credit = s_total_credit,
#         )

#         obj.save()
#         return redirect('add_voucher_list_url')
#     return render(request,'finance/voucher/add.html', context)


def fn_add_voucher_list_view(request):
    voucher = add_voucher.objects.all()
    context = {'voucher' : voucher}
    return render(request,'finance/voucher/list.html', context)

    
# @login_required(login_url='admin_login_url')
def fn_add_voucher_details_view(request,id):
    '''
    This view function for display the specific add_voucher information.
    '''
    obj = add_voucher.objects.get(id=id)
    context = {'obj':obj}
    return render(request,'finance/voucher/details.html', context)


# @login_required(login_url='admin_login_url')
def fn_add_voucher_edit_view(request,id):
    '''
    This view function for update the specific add_voucher information.
    '''
    branch = Branch.objects.all()
    form = Group.objects.all()
    voucher = add_voucher.objects.get(id=id)
    context = {'form':form,'voucher':voucher,'branch':branch}
    if request.method == 'POST':
        s_branch = Branch.objects.filter(s_Branch_City = request.POST.get('branch_city')).first()
        s_voucher_type = request.POST.get('s_voucher_type')
        d_voucher_date = request.POST.get('d_voucher_date')
        by_or_to = request.POST.get('by_or_to')
        s_perticular = request.POST.get('s_perticular')
        s_debit = request.POST.get('s_debit')
        s_credit = request.POST.get('s_credit')
        s_total_debit = request.POST.get('s_total_debit')
        s_total_credit = request.POST.get('s_total_credit')

      
        obj = add_voucher(
            id=id,
            s_branch = s_branch,          
            d_voucher_date = d_voucher_date,
            s_voucher_type = s_voucher_type,
            by_or_to = by_or_to,
            s_perticular = s_perticular,
            s_debit = s_debit,
            s_credit = s_credit,
            s_total_debit = s_total_debit,
            s_total_credit = s_total_credit,
        )

        obj.save()
        return redirect('add_voucher_list_url')
    
    return render(request,'finance/voucher/edit.html', context)


# @login_required(login_url='admin_login_url')
def fn_Add_voucher_Delete_View(request,id):
    '''
    This view function for delete the specifice add_voucher.
    '''
    obj = add_voucher.objects.get(id=id)
    obj.delete()
    return redirect('add_voucher_list_url')

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







        




        

        





