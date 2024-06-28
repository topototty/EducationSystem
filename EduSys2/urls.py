from django.contrib import admin
from django.urls import path, include
from EduSysApp import views as v
from views import *

from EduSysApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', v.registration, name='registration'),
    path('', v.login_view, name='login'),
    path('profile/<int:user_id>/', v.profile_view, name='profile'),
    path('logout/', v.logout_view, name='logout'),
    path('', include('EduSysApp.Employees.routing')),
    path('', include('EduSysApp.Students.routing')),
    path('', include('EduSysApp.Groups.routing')),
    path('', include('EduSysApp.Lessons.routing')),
    path('', include('EduSysApp.Grades.routing')),
    path('', include('EduSysApp.Requests.routing')),
]
