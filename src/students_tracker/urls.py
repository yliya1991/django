"""students_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path

from students import views

from teachers import views as t_views
from teachers import views as f_views
from group import views as g_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', t_views.index),
    path('', g_views.index),


    path('generate-student/', views.generate_student),
    path('generate-students/', views.generate_students),
    path('teachers/', t_views.teachers_generate),
    path('create1/', f_views.create_teacher),
    path('create2/', g_views.create_group),

]
