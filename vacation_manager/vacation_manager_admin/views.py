from django.views.generic import CreateView, ListView, TemplateView
import vacation_manager_admin.models as models
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"


class VacationCreateView(CreateView):
    model = models.Vacation
    template_name = "vacation/create_vacation.html"
    fields = ["name", "status", "description", "identification_number"]
    success_url = reverse_lazy("index")
