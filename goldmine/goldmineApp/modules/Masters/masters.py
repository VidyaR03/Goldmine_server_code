from django.shortcuts import render
from goldmineApp . models import *
from django.contrib.auth.decorators import login_required



# @login_required(login_url='admin_login_url')
def fn_Masters_View(request):
    accounts = Accounts.objects.all().count()
    branches = Branch.objects.all().count()
    groups = Group.objects.all().count()
    vehicles = Vehicle.objects.all().count()
    drivers = Driver.objects.all().count()
    locations = Location.objects.all().count()
    expenses = Expence.objects.all().count()
    deliver_types = Delivery_Type.objects.all().count()
    pay_types = Pay_Type.objects.all().count()
    lorry_books = Lorry_Book.objects.all().count()
    cities = City.objects.all().count()
    consignros = Consignor.objects.all().count()
    consignees = Consignee.objects.all().count()

    context = {
        'accounts' : accounts,
        'branches' : branches,
        'groups' : groups,
        'vehicles' : vehicles,
        'drivers' : drivers,
        'locations' : locations,
        'expenses' : expenses,
        'delivery_types' : deliver_types,
        'pay_types' : pay_types,
        'lorry_books' : lorry_books,
        'cities' : cities,
        'consignros':consignros,
        'consignees':consignees
        }
    
    return render(request,'masters/masters.html',context)
