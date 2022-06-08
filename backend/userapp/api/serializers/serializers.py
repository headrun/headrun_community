from dataclasses import field, fields
from rest_framework import serializers
from django.contrib.auth.models import User
from userapp.model.models import Profile
# from headrun_community.user.models.models import Profile, Posts

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('user_name')
    class Meta:
        model= Profile
        fields= ['id', 'date_of_birth','designation', 'work_location', 'user' , 'status']
        
    def user_name(self,instance):
        print("self", instance.user_id)
        try:
            return str(instance.user_id)
        except:
            return 0
        