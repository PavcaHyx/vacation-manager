from django.urls import path
import vacation_manager_admin.views as views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("vacation/create", views.VacationCreateView.as_view(), name="vacation_create")
]