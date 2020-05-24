from django.urls import path

from group import views

app_name = 'group'

urlpatterns = [
    path('list/', views.show_group, name='list'),
    path('create/', views.create_group, name='create'),
    path('edit/<int:pk>', views.edit_group, name='edit'),
    path('delete/<int:pk>', views.delete_group, name='delete'),
]
