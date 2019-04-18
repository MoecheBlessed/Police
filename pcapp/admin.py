from django.contrib import admin
from . models import Record, Criminal, Staff, Crime

# Register your models here.
admin.site.register(Record)
admin.site.register(Criminal)
admin.site.register(Staff)
admin.site.register(Crime)
