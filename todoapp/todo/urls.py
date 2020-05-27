from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('updatetask/<int:pk>/', views.updatetask, name='updatetask'),
]
