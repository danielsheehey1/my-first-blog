from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment, Machine, Customer, Employee, Work_Order, Work_Order_Item

class EmployeeForm(forms.ModelForm):
    employee_select = forms.ModelChoiceField(queryset = User.objects.all())

    class Meta:
        model = Employee
        exclude = ('name','assigned',)

class Work_OrderForm(forms.ModelForm):

    class Meta:
        model = Work_Order
        fields = '__all__'

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name',)

class MachineForm(forms.ModelForm):

    class Meta:
        model = Machine
        fields = '__all__' #('make', 'model', 'customer', 'serial', 'hours',)
