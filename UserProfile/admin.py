from django.contrib import admin

from .models import Profile, status, friend, notification,  coverphotos,profilephotos


class statusAdmin(admin.ModelAdmin):
    list_display=['post','date','day','time']
admin.site.register(Profile)
admin.site.register(status,statusAdmin)
admin.site.register(friend)
admin.site.register(notification)

admin.site.register(coverphotos)
admin.site.register(profilephotos)

