from django.urls import path
from games import views

urlpatterns = [
    path('v1/', views.GameList.as_view()),
    path('v1/<int:pk>/', views.GameDetail.as_view()),
]