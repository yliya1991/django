from django.urls import path

from teachers import views

app_name = 'teachers'

urlpatterns = [
    path('list/', views.show_teachers, name='list'),
    path('create/', views.create_teacher, name='create'),
    path('edit/<int:pk>', views.edit_teacher, name='edit'),
    path('delete/<int:pk>', views.delete_teacher, name='delete'),
<<<<<<< HEAD
    path('email/', views.email, name='email'),
=======
>>>>>>> a8aa4e4ba879bca99be5dfe897736f99e6750c8e
]
