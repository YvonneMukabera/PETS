from django.shortcuts import render
from .models import Expense

def expenselist(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expenselist.htm', {'expenses': expenses})
