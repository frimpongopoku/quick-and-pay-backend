from invoice.Serializers import InvoiceSheetSerializer
from invoice.helpers.return_ticket import TransferResponse
from invoice.models import InvoiceSheet


class InvoiceSheetHandler:
  model = InvoiceSheet
  serializer = InvoiceSheetSerializer
  
  @staticmethod
  def createNewInvoiceSheet(data):
    if not data: return TransferResponse(error="Data is empty...")
    # ser = InvoiceSheetHandler.serializer(data=data)
    # if ser.is_valid():
    #   ser.save()
    #   return TransferResponse(data=ser.data)
    # return TransferResponse(error=str(ser.errors))
    instance = InvoiceSheetHandler.model()
    instance.id = data.get("id")
    instance.title = data.get("title") or "Default title"
    instance.currency = data.get("currency") or "$"
    instance.description = data.get("description") or "Default description..."
    instance.payer_email = data.get("payer_email")
    instance.payer_name = data.get("payer_name") or " @default - Akwesi payer"
    instance.payee_middle_name = data.get("payee_middle_name") or "@middle_name"
    instance.payee_last_name = data.get("payee_last_name") or "@last Name"
    instance.due_date = data.get("due_date")
    instance.total_amount_payable = data.get("total_amount_payable")
    instance.phone_number = data.get("phone_number")
    instance.save()
    return TransferResponse(data=instance)
  
  # @staticmethod
  # def get_sheet_instance(data):
  #   instance = InvoiceSheetHandler.model()
  #   instance.id = data["id"]
  #   instance.title = data["title"]
  #   instance.currency = data["currency"]
  #   instance.description = data["description"]
  #   instance.payer_email = data["payer_email"]
  #   instance.payer_name = data["payer_name"]
  #   instance.payee_middle_name = data["payee_middle_name"]
  #   instance.payee_last_name = data["payee_last_name"]
  #   instance.due_date = data["due_date"]
  #   instance.total_amount_payable = data["total_amount_payable"]
  #   instance.phone_number = data["phone_number"]
  #   return instance
