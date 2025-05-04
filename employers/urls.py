from django.urls import path
from .views import EmployerCreateListView, EmployerDetailView

urlpatterns = [
    path('', EmployerCreateListView.as_view()),
    path('<int:pk>/', EmployerDetailView.as_view()),
]