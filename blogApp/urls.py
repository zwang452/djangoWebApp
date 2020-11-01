from django.urls import path

from . import views

urlpatterns = [
    # ex: /blogApp/
    path('', views.index, name='index'),
    # ex: /blogApp/post_id
    path('<int:post_id>/', views.detail, name='detail'),
]