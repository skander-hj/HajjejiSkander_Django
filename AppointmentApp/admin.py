from django.contrib import admin
from .models import Appointment

# Register your models here.
@admin.register(Appointment)
class AppointmentAdminPerso(admin.ModelAdmin):
    list_display = (
        'id', 'reason', 'status',
        'duration_minutes', 'appointment_date',
        'doctor', 'patient',
    ) 
    list_filter = ('status', 'doctor', 'patient')
    list_editable = ('status',)
    search_fields = ('doctor__username',)
    list_per_page = 2 
    ordering = ('appointment_date',)

    fieldsets = (
        ('Appointment Information', {
        'fields': ('reason', 'status')
        }),
        ('Appointment Details', {
        'fields': ('duration_minutes',
        'appointment_date', 'doctor', 'patient')
        }),
        ('Non Editable', {
        'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')