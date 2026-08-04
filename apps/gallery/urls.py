from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('album/create/', views.album_create, name='album_create'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('album/<int:album_pk>/upload/', views.photo_upload, name='photo_upload'),
]
