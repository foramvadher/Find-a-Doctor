from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Contact)
admin.site.register(Language)
admin.site.register(District)
admin.site.register(Specialization)
admin.site.register(Availability)

