"""import topic"""
from django.contrib import admin
from .models import LessonTopics, TagsModel, Letters


admin.site.register(LessonTopics)
admin.site.register(TagsModel)
admin.site.register(Letters)
