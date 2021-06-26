from rest_framework import serializers

from invoice.models import InvoiceSheet, InvoiceItem


class InvoiceSheetSerializer(serializers.ModelSerializer):
  model = InvoiceSheet
  fields = "__all__"


class InvoiceItemSerializer(serializers.ModelSerializer):
  moel = InvoiceItem
  fields = "__all__"
