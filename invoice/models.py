from django.db import models


# Create your models here.

class InvoiceItem(models.Model):
  description = models.TextField(null=False, blank=False)
  quantity = models.IntegerField(blank=True, null=True, default=1)
  price = models.IntegerField(blank=False, null=False)


class InvoiceSheet(models.Model):
  title = models.CharField(max_length=300, blank=True, null=False)
  currency = models.CharField(max_length=100, blank=True, null=False)
  description = models.TextField(blank=True, null=True)
  payer_name = models.CharField(max_length=300, blank=True, null=False)
  payer_email = models.EmailField()
  payer_address = models.TextField()
  phone_number = models.CharField(max_length=100, blank=True, null=True)
  due_date = models.CharField(max_length=300, blank=True, null=True)
  total_amount_payable = models.IntegerField(blank=True, null=False, default=0)
  invoice_items = models.ForeignKey(InvoiceItem, on_delete=models.CASCADE, related_name="invoice_sheet")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
