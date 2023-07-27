from django.shortcuts import render,redirect
from goldmineApp . models import *

def fn_profit_loss_View(request):
   expense = Trip_Sheet.objects.all()
   income = Invoice.objects.all()
   
   context = {
     'expense':expense,
     'income':income,
        
    }
   return render(request,'finance/profit_loss/list_profit_loss.html',context)