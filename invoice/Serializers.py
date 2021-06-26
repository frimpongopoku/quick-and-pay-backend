from rest_framework import serializers

from invoice.models import InvoiceSheet, InvoiceItem


class InvoiceSheetSerializer(serializers.ModelSerializer):

  class Meta:
    model = InvoiceSheet
    fields = "__all__"
  
   
    

class InvoiceItemSerializer(serializers.ModelSerializer):

  class Meta:
    model = InvoiceItem
    fields = "__all__"

