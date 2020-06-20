from django.contrib import admin
from .models import Notice


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('notice_title','updated_date',)

admin.site.register(Notice,NoticeAdmin)