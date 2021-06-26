from django.http import JsonResponse


class ReturnTicket(JsonResponse):
  def __init__(self, data=None, error=None, status=200, ):
    errorObj = {"status": True if error is not None else False, "message": error}
    response = {"data": data, "error": errorObj, "success": not error}
    super().__init__(
      response,
      safe=True,
      status=status
    )


class TransferResponse:
  def __init__(self, data=None, raw=None, ok=True, error=None):
    self.data = data
    self.raw = raw
    self.ok = False if error else True
    self.error = error
  
  def isOkay(self):
    return self.ok
  
  def data(self):
    return self.data
  
  def raw(self):
    return self.raw
  
  def error(self):
    return self.error