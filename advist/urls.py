from django.urls import path
from . import views
from .views import index, by_rubric
app_name = 'advist'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:rubric.id>/', views.by_rubric, name='by_rubric'),
]

