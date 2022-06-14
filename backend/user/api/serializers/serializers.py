from dataclasses import field, fields
from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import Profile
# from headrun_community.user.models.models import Profile, Posts


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


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
        