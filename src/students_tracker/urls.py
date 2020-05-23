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
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
<<<<<<< HEAD
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from teachers import views
=======
from django.contrib import admin
from django.urls import include, path

from students import views
>>>>>>> a8aa4e4ba879bca99be5dfe897736f99e6750c8e

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teachers/', include('teachers.urls')),
    path('group/', include('group.urls')),
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('email/', views.email, name='email'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
=======

    path('students/', include('students.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
>>>>>>> a8aa4e4ba879bca99be5dfe897736f99e6750c8e
