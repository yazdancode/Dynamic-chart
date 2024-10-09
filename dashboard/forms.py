from django import forms
from .models import LessonScore


class LessonForm(forms.ModelForm):
    class Meta:
        model = LessonScore
        fields = "__all__"
        labels = {
            "lesson": "Lesson Name",
            "score": "Score",
        }
