from django.urls import path
from . import views

urlpatterns = [
        path('sites/list',views.index, name='index'),
		path('sites', views.addNote, name="create"),
        ]
