from django.contrib import admin
from .models import Lesson, LessonScore


class LessonScoreAdmin(admin.ModelAdmin):
    list_display = ("lesson", "score")


admin.site.register(Lesson, admin.ModelAdmin)
admin.site.register(LessonScore, LessonScoreAdmin)
