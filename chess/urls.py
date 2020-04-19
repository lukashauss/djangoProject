from django.urls import path
from . import views

app_name = 'chess'

urlpatterns = [
    path('', views.home),
    path('selectField', views.selectField),
    path('move', views.move),
    path('moveable', views.returnMoveable),
]