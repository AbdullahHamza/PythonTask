from django.contrib import admin
from django.urls import path, include
from employee.views import AttendanceView, CheckAttendanceView
urlpatterns = [
    path('history', AttendanceView.as_view()),
    path('actions', CheckAttendanceView.as_view())
]
