from django.contrib import admin
from .models import *
# Register your models here.



class AttendanceActionsInline(admin.TabularInline):
    model = AttendanceActions
    extra = 0


class AttendanceAdmin(admin.ModelAdmin):
    inlines = [AttendanceActionsInline]


admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AttendanceActions)
