from goldmineApp . models import Expence
import datetime
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required


# @login_required(login_url='admin_login_url')
def fn_Expence_Add_View(request):
    '''
    This view function for add the new expence.
    '''
    if request.method == 'POST':
        s_Expence = request.POST.get('expence')
        s_Date = datetime.datetime.today()

        e = Expence(
            s_Expence=s_Expence,
            s_Date=s_Date
            )

        e.save()
        return redirect('expence_list_view')

    return render(request,'masters/expense/add.html')


# @login_required(login_url='admin_login_url')
def fn_Expence_List_View(request):
    '''
    This view function for display all the expences.
    '''
    form = Expence.objects.all()
    context = {'form':form}
    return render(request, 'masters/expense/list.html',context)


# @login_required(login_url='admin_login_url')
def fn_Expence_Update_View(request,id):
    '''
    This view function for update the data of specific expence.
    '''
    obj = Expence.objects.get(id=id)
    context = {'obj':obj}
    if request.method == 'POST':
        s_Expence = request.POST.get('expence')
        s_Date = request.POST.get('date')

        e = Expence(
            id=id,
            s_Expence=s_Expence,
            s_Date=s_Date
            )

        e.save()
        return redirect('expence_list_view')

    return render(request,'masters/expense/update.html',context)


# @login_required(login_url='admin_login_url')
def fn_Expence_Delete_View(request,id):
    '''
    This view function for delete the specific expence.
    '''
    obj = Expence.objects.get(id=id)
    obj.delete()
    return redirect('expence_list_view')
