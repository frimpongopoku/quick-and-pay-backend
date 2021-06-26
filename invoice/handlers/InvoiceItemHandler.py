from invoice.Serializers import InvoiceItemSerializer
from invoice.helpers.return_ticket import TransferResponse
from invoice.models import InvoiceItem


class InvoiceItemHandler:
  model = InvoiceItem
  serializer = InvoiceItemSerializer
  
  @staticmethod
  def createMultipleItems(array, sheet):
    if not sheet: return TransferResponse(error="Provide an instance of a sheet model...")
    if not array: return TransferResponse(error="Data is empty...")
    for item in array:
      InvoiceItemHandler.createNewItem(item,sheet)
    return TransferResponse()
  
  @staticmethod
  def createNewItem(data, sheet):
    if not data: return TransferResponse(error="Data is empty...")
    ser = InvoiceItemHandler.serializer(data)
    new_invoice = InvoiceItemHandler.model()
    new_invoice.description = data["description"]
    new_invoice.price = data["price"]
    new_invoice.quantity = data["quantity"]
    new_invoice.invoice_sheet = sheet
    new_invoice.save()
    return TransferResponse()
    
