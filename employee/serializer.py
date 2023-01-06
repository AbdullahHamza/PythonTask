from rest_framework import serializers

class AttendanceActionsSerializer(serializers.Serializer):
    action = serializers.CharField()
    time = serializers.DateTimeField(source= "action_time")



class AttendanceSerializer(serializers.Serializer):

    date = serializers.DateField(source= "day")
    actions = serializers.SerializerMethodField()

    def get_actions(self, obj):
        return AttendanceActionsSerializer(obj.attendance_action.all(), many=True).data


