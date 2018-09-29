from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='portal_index'),
    # path('image_list/', views.image_list, name='image_list'),
]