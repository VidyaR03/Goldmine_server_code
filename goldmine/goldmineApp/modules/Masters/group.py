from goldmineApp . models import Group
import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# @login_required(login_url='admin_login_url')
def fn_Group_Add_View(request):
    '''
    This view function for add group data.
    '''
    if request.method == 'POST':
        s_Group_Name = request.POST.get('group_name')
        s_Date = request.POST.get('current_date')

        obj = Group(
            s_Group_Name=s_Group_Name,
            s_Date=s_Date
            )

        obj.save()
        return redirect('group_list_url')

    return render(request,'masters/groups/add.html')


# @login_required(login_url='admin_login_url')
def fn_Group_List_View(request):
    '''
    This view function view for display all data of group.
    '''
    form = Group.objects.all()
    context = {'form':form}
    return render(request,'masters/groups/list.html',context)


# @login_required(login_url='admin_login_url')
def fn_Group_Update_View(request,id):
    '''
    This view function for update the specific group data.
    '''
    obj = Group.objects.get(id=id)
    context = {'obj':obj}
    if request.method == 'POST':
        s_Group_Name = request.POST.get('group_name')
        s_Date = datetime.datetime.today()

        obj = Group(
            id=id,
            s_Group_Name=s_Group_Name,
            s_Date=s_Date
            )
        obj.save()
        return redirect('group_list_url')

    return render(request,'masters/groups/update.html',context)


# @login_required(login_url='admin_login_url')
def fn_Group_Delete_View(request,id):
    '''
    This view function for delete the specific group data.
    '''
    obj = Group.objects.get(id=id)
    obj.delete()
    return redirect('group_list_url')
