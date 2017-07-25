from django.contrib import admin
from .models import  Machine, Customer, Employee, Work_Order, Work_Order_Item, Person

admin.site.register(Customer)
admin.site.register(Machine)
admin.site.register(Work_Order)
admin.site.register(Work_Order_Item)
admin.site.register(Employee)
admin.site.register(Person)
