from django.contrib import admin
from .models import *



# admin.site.register(Order)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["size", "status", "quantity", "created_at"]
    list_filter = ["created_at", "status", "size"]