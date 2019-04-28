from django.urls import path, include
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.landing, name='landing'),
    path('<int:blog_id>', views.detail, name='detail'),
]
