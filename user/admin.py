from django.contrib import admin

from .models import UserInfo, HealthInformation


class UserInfoAdmin(admin.ModelAdmin):
    pass



class HealthInformationAdmin(admin.ModelAdmin):
    pass



admin.site.site_header = '心血管疾病检测网站后台管理'
admin.site.site_title = '心血管疾病检测网站后台管理'

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(HealthInformation, HealthInformationAdmin)
