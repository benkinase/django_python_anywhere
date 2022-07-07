from rest_framework import serializers
from .models import Interview, Application,Techstack

class TechstackSerializer(serializers.ModelSerializer):

  class Meta:
    model = Techstack
    fields = ('__all__')

# class ScheduleSerializer(serializers.ModelSerializer):
#   job_title=serializers.ReadOnlyField(source='application.job_title')
#   company=serializers.ReadOnlyField(source='application.company')

#   class Meta:
#     model = Schedule
#     fields = ('__all__')


class InterviewSerializer(serializers.ModelSerializer):
  #application=serializers.SerializerMethodField('getApp')
  job_title=serializers.ReadOnlyField(source='application.job_title')
  company=serializers.ReadOnlyField(source='application.company')
  #date=serializers.DateField(format="%d-%m-%Y",read_only=True)

  class Meta:
    model = Interview
    fields = ('__all__')


class ApplicationSerializer(serializers.ModelSerializer):
  techstack=TechstackSerializer(many=True, read_only=True)
  interviews=InterviewSerializer(many=True, read_only=True)
  #schedules=ScheduleSerializer(many=True, read_only=True)

  class Meta:
    model = Application
    fields = ('__all__')




