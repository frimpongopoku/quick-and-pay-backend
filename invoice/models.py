from django.db import models
from random import randint


# Create your models here.


class InvoiceSheet(models.Model):
  title = models.CharField(max_length=300, blank=True, null=False)
  currency = models.CharField(max_length=100, blank=True, null=False)
  description = models.TextField(blank=True, null=True, default="Default description...")
  payee_name = models.TextField(blank=False, null=False, default=f"User - {str(randint(0, 999999))} - @default-first")
  payee_middle_name = models.TextField(blank=False, null=False,
                                       default=f"User - {str(randint(0, 999999))} - @default-middle")
  payee_last_name = models.TextField(blank=False, null=False,
                                     default=f"User - {str(randint(0, 999999))} - @default-last")
  payer_name = models.CharField(max_length=300, blank=False, null=False, default="Some Person...")
  payer_email = models.EmailField()
  payer_address = models.TextField()
  phone_number = models.CharField(max_length=100, blank=True, null=True)
  due_date = models.CharField(max_length=300, blank=True, null=True)
  total_amount_payable = models.IntegerField(blank=True, null=False, default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f"Invoice #{str(self.id)} to {self.payer_name} from {self.payee_name}. Total : {self.total_amount_payable}"


class InvoiceItem(models.Model):
  description = models.TextField(null=False, blank=False)
  quantity = models.IntegerField(blank=True, null=True, default=1)
  price = models.IntegerField(blank=False, null=False)
  invoice_sheet = models.ForeignKey(InvoiceSheet, on_delete=models.CASCADE, related_name="invoice_items", default=None)
  
  def __str__(self):
    return self.description
