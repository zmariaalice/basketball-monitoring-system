from django.urls import path
from .views import LoginListCreateView, LoginDetailView

urlpatterns = [
    path('', LoginListCreateView.as_view(), name='login-list-create'),
    path('<int:pk>/', LoginDetailView.as_view(), name='login-detail'),
]
