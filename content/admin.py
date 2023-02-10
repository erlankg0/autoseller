from django.contrib import admin
from content.models import Phone, Address, Email, Logo, WorkTime, TechCenter, Whatsapp, Title, Banner
from content.models import About, Images, Best


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass


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


@admin.register(Whatsapp)
class WhatsappAdmin(admin.ModelAdmin):
    list_display = ('number',)
    search_fields = ('number',)
    list_filter = ('number',)
    ordering = ('number',)


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)


@admin.register(Best)
class BestAdmin(admin.ModelAdmin):
    pass


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]
