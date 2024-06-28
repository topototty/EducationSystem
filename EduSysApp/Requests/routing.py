from django.contrib import admin
from django.urls import path, include
from EduSysApp.Requests import views as v
from .views import *
from EduSysApp.views import *

urlpatterns = [
    path('requests/', v.request_list, name='requests'),
    path('add_request/', AddRequestView.as_view(), name='add_request'),
    path('edit_request/<int:request_id>/', EditRequestView.as_view(), name='edit_request'),
    path('requests_for_employee/', v.request_list_for_employee, name='requests_for_employee'),

]
