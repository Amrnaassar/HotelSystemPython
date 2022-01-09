from django.contrib import admin
from .models import booking
from .models import room
# Register your models here.
admin.site.register(booking)
admin.site.register(room)