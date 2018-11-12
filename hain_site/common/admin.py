from django.contrib import admin
from .models import AboutMembers, Updates, Career

# Register your models here.
admin.site.register(AboutMembers)
admin.site.register(Updates)
admin.site.register(Career)