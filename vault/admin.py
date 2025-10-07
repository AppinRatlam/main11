from django.contrib import admin
from .models import Devotee, Deposit

@admin.register(Devotee)
class DevoteeAdmin(admin.ModelAdmin):
    list_display = ('name','phone','aadhaar_last4','created_at')
    search_fields = ('name','phone','aadhaar_last4')

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('token','devotee','amount','status','received_at','returned_at','diwali_year')
    list_filter = ('status','diwali_year','received_at')
    search_fields = ('token','devotee__name','devotee__phone')
