from django.shortcuts import render

# Create your views here.
def home_screen_view(request):
  print(request.headers)
  return render(request, "base.html", {})

def home_screen_view(request):
  context = {}
  return render(request, "templates/cart.html", context)

def home_screen_view(request):
  context = {}
  return render(request, "templates/checkout.html", context)

def home_screen_view(request):
  context = {}
  return render(request, "templates/store.html", context)