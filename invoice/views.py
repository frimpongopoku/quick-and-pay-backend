from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view

from invoice.decorators import has_fields
from invoice.helpers.return_ticket import ReturnTicket


@api_view(["POST"])
@has_fields(["booty"])
def test_app(request):
  return ReturnTicket(data = f"Yes, we found the fields bro {request.data.get('booty')}")
  