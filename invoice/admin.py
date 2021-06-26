from django.contrib import admin
from invoice.models import InvoiceItem, InvoiceSheet
# Register your models here.
admin.site.register(InvoiceItem)
admin.site.register(InvoiceSheet)