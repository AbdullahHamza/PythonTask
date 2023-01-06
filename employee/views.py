from django.shortcuts import render
from rest_framework.views import APIView
from employee.models import *
from employee.serializer import AttendanceSerializer, AttendanceActionsSerializer
from rest_framework.response import Response
from datetime import datetime, timedelta
class AttendanceView(APIView):
    
    def get(self, req):
        employee_code= req.GET.get("employee_code")
        query = Attendance.objects.filter(employee=employee_code)
        output = AttendanceSerializer(query, many=True).data
        return Response({'days':output})



class CheckAttendanceView(APIView):
    
    def get(self, req):
        employee_code= req.GET.get("employee_code")
        today = datetime.strptime(req.GET.get("date"), "%Y-%m-%d")
        yesterday = today - timedelta(days=1)

        today_attendance = Attendance.objects.filter(employee=employee_code, day= today).first()
        yesterday_attendance = Attendance.objects.filter(employee=employee_code, day=yesterday).first()

        hours=0
        min=0
        duration=""

                

        if today_attendance:
            today_acctions = today_attendance.attendance_action.all().order_by('action_time')
            
            if today_acctions[0].action == "CheckOut":
                hours += today_acctions[0].action_time.hour
                min +=  today_acctions[0].action_time.minute
                today_acctions.pop(0)

            index=0

            while index<len(today_acctions):


                if index+1 == len(today_acctions):
                    hours += 23- today_acctions[index].action_time.hour
                    min += 60- today_acctions[index].action_time.minute
                else:
                    hours += today_acctions[index+1].action_time.hour - today_acctions[index].action_time.hour
                    min += today_acctions[index+1].action_time.minute - today_acctions[index].action_time.minute
                
                index+=2


        hours+= int(min/60)
        min= min%60

        if hours ==0 and min==0:
            output = {'attended':False, 'duration': '00:00'}
        else:
            duration= str(hours)+":"+str(min)
            output = {'attended':True, 'duration': duration}


        return Response(output)