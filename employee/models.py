from django.db import models
from django.utils import timezone

#Attendance Model
class Attendance(models.Model):
    day = models.DateField(default=timezone.now)
    employee = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)


#AttendanceActions Model
class AttendanceActions(models.Model):
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name="attendance_action")
    action_time = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)