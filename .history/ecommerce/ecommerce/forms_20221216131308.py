from django.forms import ModelForm
from .models import Odrder
from django.contrib.auth.forms import UserCreationForm

class OrderForm(ModelForm):
  class Meta:
    model = OrderForm
    fields = '__all__'