from django.db import models
from django.db.models import Avg


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام درس")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "درس‌ها"
        verbose_name_plural = "درس‌ها"


class LessonScore(models.Model):
    lesson = models.ForeignKey(to=Lesson, on_delete=models.PROTECT, verbose_name="درس")
    score = models.IntegerField(verbose_name="نمرات")

    def __str__(self):
        return f"{self.lesson} - {self.score}"

    @classmethod
    def average_score(cls, lesson_id):
        avg_score = cls.objects.filter(lesson_id=lesson_id).aggregate(Avg("score"))[
            "score__avg"
        ]
        return avg_score if avg_score is not None else 0

    class Meta:
        verbose_name = "نمره درس‌ها"
        verbose_name_plural = "نمره درس‌ها"
