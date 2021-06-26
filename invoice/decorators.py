from invoice.helpers.return_ticket import ReturnTicket


def has_fields(array):
  def wrapper(function):
    def runner(request):
      for field in array:
        if not request.data.get(field): return ReturnTicket(error=f"'{field}' field is required, please provide...")
      return function(request)
    
    return runner

  return wrapper
