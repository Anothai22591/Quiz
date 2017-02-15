from django.contrib import admin

from .models import Question,Group,Choice

admin.site.register(Group)
admin.site.register(Question)
admin.site.register(Choice)
