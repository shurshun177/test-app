from django.shortcuts import render
from .models import Expense

# Create your views here.
def expense_list(request):
    expenses = Expense.objects.order_by('-date')
    return render(request, 'MyExpenses/expense_list.html', {'expenses': expenses})