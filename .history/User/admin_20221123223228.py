from django.contrib import admin
from .models import lastname, firstname, phone, email, gender, address

admin.site.register(lastname)
admin.site.register(firstname)
admin.site.register(phone)
admin.site.register(email)
admin.site.register(gender)
admin.site.register(address)