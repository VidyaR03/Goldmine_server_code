from goldmineApp . models import City
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# @login_required(login_url='admin_login_url')
def fn_City_Add_View(request):
    '''
    This view function for add new city.
    '''
    if request.method == 'POST':
        s_City_Name = str.capitalize(request.POST.get('city'))
        s_State = str.capitalize(request.POST.get('state'))

        e = City(
            s_City_Name=s_City_Name,
            s_State=s_State
            )

        e.save()
        return redirect('city_list_url')

    return render(request,'masters/cities/add.html')



# @login_required(login_url='admin_login_url')
def fn_City_List_View(request):
    '''
    This view function for display all the cities.
    '''
    form = City.objects.all()
    context = {'form':form}
    return render(request,'masters/cities/list.html',context)



# @login_required(login_url='admin_login_url')
def fn_City_Update_View(request,id):
    '''
    This view function for update the specific city.
    '''
    obj = City.objects.get(id=id)
    context = {'obj':obj}
    if request.method == 'POST':
        s_City_Name = str.capitalize(request.POST.get('city'))
        s_State = str.capitalize(request.POST.get('state'))

        e = City(
            id=id,
            s_City_Name=s_City_Name,
            s_State=s_State
            )

        e.save()
        return redirect('city_list_url')

    return render(request,'masters/cities/update.html',context)



# @login_required(login_url='admin_login_url')
def fn_City_Delete_View(request,id):
    '''
    This view function for delete the specific city.
    '''
    obj = City.objects.get(id=id)
    obj.delete()
    return redirect('city_list_url')
