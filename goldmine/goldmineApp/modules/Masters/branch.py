from goldmineApp . models import Branch
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required


# @login_required(login_url='admin_login_url')
def fn_Branch_Add_View(request):
    '''
    This view function for add the new branch.
    '''
    if request.method == 'POST':
        s_Branch_Address = request.POST.get('branch_address')
        s_Branch_City = str.capitalize(request.POST.get('branch_city'))
        s_Branch_State = str.capitalize(request.POST.get('branch_state'))

        obj = Branch(
            s_Branch_Address=s_Branch_Address,
            s_Branch_City=s_Branch_City,
            s_Branch_State=s_Branch_State
            )
        
        obj.save()
        return redirect('branch_list_url')
    
    return render(request,'masters/branches/add.html')


# @login_required(login_url='admin_login_url')
def fn_Branch_List_View(request):
    '''
    This view function for display the all branches.
    '''
    form = Branch.objects.all()
    context = {'form':form}
    return render(request,'masters/branches/list.html',context)


# @login_required(login_url='admin_login_url')
def fn_Branch_Update_View(request,id):
    '''
    This view function for update the data of specific branch.
    '''
    obj = Branch.objects.get(id=id)
    context = {'obj':obj}
    if request.method == 'POST':
        s_Branch_Address = request.POST.get('branch_address')
        s_Branch_City = str.capitalize(request.POST.get('branch_city'))
        s_Branch_State = str.capitalize(request.POST.get('branch_state'))
        obj = Branch(
            id=id,
            s_Branch_Address=s_Branch_Address,
            s_Branch_City=s_Branch_City,
            s_Branch_State=s_Branch_State
            )

        obj.save()
        return redirect('branch_list_url')

    return render(request,'masters/branches/update.html',context)


# @login_required(login_url='admin_login_url')
def fn_Branch_Delete_View(request,id):
    '''
    This view function for delete the specific branch.
    '''
    obj = Branch.objects.get(id=id)
    obj.delete()
    return redirect('branch_list_url')
