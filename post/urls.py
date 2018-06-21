from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('post/detail/<int:id>', views.detail, name='detail'),
]