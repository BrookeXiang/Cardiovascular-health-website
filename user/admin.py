from django.contrib import admin

from .models import UserInfo, HealthInformation


class UserInfoAdmin(admin.ModelAdmin):
    pass



class HealthInformationAdmin(admin.ModelAdmin):
    pass



admin.site.site_header = 'ADMIN'
admin.site.site_title = 'ADMIN'

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(HealthInformation, HealthInformationAdmin)
