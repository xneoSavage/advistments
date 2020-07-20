from django.urls import path
from . import views
app_name = 'advist'
urlpatterns = [
    path('', views.index, name='advist_list'),
]

