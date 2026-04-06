from django.shortcuts import render
from .models import Expense

def expenselist(request):
    expenses = Expense.objects.all()
    #calculate total expenses
    total= sum(expense.amount for expense in expenses)
    return render(request, 'expenses/expenselist.htm', {
        'expenses': expenses, 
        'total': total
    })
