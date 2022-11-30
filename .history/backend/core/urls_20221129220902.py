from django.contrib import admin
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('.*', TemplateView.as_view(template_name='index')),
]