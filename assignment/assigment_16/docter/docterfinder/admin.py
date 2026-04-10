from django.contrib import admin
from docterfinder.models  import Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'email', 'phone')

admin.site.register(Doctor, DoctorAdmin)