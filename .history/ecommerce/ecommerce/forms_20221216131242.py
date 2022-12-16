from django.forms import ModelForm
from .models import Odrder

class OrderForm(ModelForm):
  class Meta:
    model = OrderForm
    fields = '__all__'