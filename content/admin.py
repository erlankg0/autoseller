from django.contrib import admin
from content.models import Phone, Address, Email, Logo, WorkTime, TechCenter


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('number',)
    search_fields = ('number',)
    list_filter = ('number',)
    ordering = ('number',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address',)
    search_fields = ('address',)
    list_filter = ('address',)
    ordering = ('address',)


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)
    list_filter = ('email',)
    ordering = ('email',)


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkTime)
class WorkTimeAdmin(admin.ModelAdmin):
    pass


@admin.register(TechCenter)
class TechCenterAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('title',)
