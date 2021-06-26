from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view

from invoice.decorators import has_fields
from invoice.handlers.InvoiceItemHandler import InvoiceItemHandler
from invoice.handlers.InvoiceSheetHandler import InvoiceSheetHandler
from invoice.helpers.return_ticket import ReturnTicket


@api_view(["POST"])
@has_fields(["energy"])
def test_app(request):
  return ReturnTicket(data=f"Yes, we found the fields bro {request.data.get('energy')}")


@api_view(["POST"])
@has_fields(["invoice_sheet", "invoice_items"])
def send_invoice(request):
  invoice_sheet_data = request.data.get("invoice_sheet")
  invoice_items = request.data.get("invoice_items")
  sheetSaveResult = InvoiceSheetHandler.createNewInvoiceSheet(invoice_sheet_data)
  if sheetSaveResult.ok:
    InvoiceItemHandler.createMultipleItems(invoice_items, sheetSaveResult.data)
  return ReturnTicket(error=sheetSaveResult.error)
