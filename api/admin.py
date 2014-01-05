from django.contrib import admin
from api.models import APIConnection

class APIAdmin(admin.ModelAdmin):
    model = APIConnection

admin.site.register(APIConnection, APIAdmin)

# Register your models here.
