from django.contrib import admin
from .models import Barangay, Business, Category, Notification, Payment, BusinessCategory, Qrcode

admin.site.register(Business)
admin.site.register(Category)
admin.site.register(Barangay)
admin.site.register(Payment)
admin.site.register(BusinessCategory)
admin.site.register(Notification)
admin.site.register(Qrcode)