from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import LessonForm
from .models import Lesson, LessonScore


class IndexView(TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lessons"] = Lesson.objects.all()
        context["form"] = LessonForm()
        context["average_scores"] = {
            lesson.id: LessonScore.average_score(lesson.id)
            for lesson in context["lessons"]
        }
        return context

    def post(self, request, *args, **kwargs):
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        return self.get(request, *args, **kwargs)
