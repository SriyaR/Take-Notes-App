from django.urls import include, path
from . import views

urlpatterns = [
		path('user/auth', views.login,name='login'),
		path('user',views.register,name='register'),
        ]
