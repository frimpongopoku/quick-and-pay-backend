from invoice.Serializers import InvoiceSheetSerializer
from invoice.helpers.return_ticket import TransferResponse
from invoice.models import InvoiceSheet


class InvoiceSheetHandler:
  model = InvoiceSheet
  serializer = InvoiceSheetSerializer
  
  @staticmethod
  def createNewInvoiceSheet(data):
    if not data: return TransferResponse(error="Data is empty...")
    ser = InvoiceSheetHandler.serializer(data)
    if ser.is_valid():
      ser.save()
      return TransferResponse()
    return TransferResponse(error=str(ser.errors))
