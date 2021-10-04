from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('full_report', views.full, name='full')
]
