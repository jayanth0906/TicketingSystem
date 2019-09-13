from django.contrib import admin
from .models import Customer, Items, Tickets


class CustomerList(admin.ModelAdmin):
    list_display = ('cust_number', 'name', 'city', 'cell_phone')
    list_filter = ('cust_number', 'name', 'city')
    search_fields = ('cust_number', 'name')
    ordering = ['cust_number']


class ItemsList(admin.ModelAdmin):
    list_display = ('Item_Id','customer', 'Type', 'Model',)
    list_filter = ('Item_Id','customer', 'Type')
    search_fields = ('Item_Id','customer', 'Type')
    ordering = ['Item_Id']


class TicketsList(admin.ModelAdmin):
    list_display = ('customer','items','Issue', 'severity','Ticket_date')
    list_filter = ('customer','items','Issue', 'severity')
    search_fields =('customer','items','Issue', 'severity')
    ordering = ['customer']


admin.site.register(Customer, CustomerList)
admin.site.register(Items, ItemsList)
admin.site.register(Tickets, TicketsList)

