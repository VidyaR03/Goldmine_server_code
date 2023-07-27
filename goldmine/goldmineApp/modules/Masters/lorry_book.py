from goldmineApp . models import Lorry_Book
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required


# @login_required(login_url='admin_login_url')
def fn_Lorry_Book_Add_View(request):
    '''
    This view function for add new lorry book.
    '''
    if request.method == 'POST':
        s_Start = request.POST.get('start')
        s_End = request.POST.get('end')

        l = Lorry_Book(
            s_Start=s_Start,
            s_End=s_End
            )

        l.save()
        return redirect('lorrybook_list_url')

    return render(request,'masters/lorry_book/add.html')
        

# @login_required(login_url='admin_login_url')
def fn_Lorry_Book_List_View(request):
    '''
    This view function for display all lorry books.
    '''
    form = Lorry_Book.objects.all()
    context = {'form':form}
    return render(request,'masters/lorry_book/list.html',context)


# @login_required(login_url='admin_login_url')
def fn_Lorry_Book_Update_View(request,id):
    '''
    This view function for update specific lorry book.
    '''
    obj = Lorry_Book.objects.get(id=id)
    context = {'obj':obj}
    if request.method == 'POST':
        s_Start = request.POST.get('start')
        s_End = request.POST.get('end')  

        obj = Lorry_Book(
            id=id,
            s_Start=s_Start,
            s_End=s_End
            )

        obj.save()
        return redirect('lorrybook_list_url')

    return render(request,'masters/lorry_book/update.html',context)
    

# @login_required(login_url='admin_login_url')
def fn_Lorry_Book_Delete_View(request,id):
    '''
    This view function for delete the specific lorry book.
    '''
    obj = Lorry_Book.objects.get(id=id)
    obj.delete()
    return redirect('lorrybook_list_url')

