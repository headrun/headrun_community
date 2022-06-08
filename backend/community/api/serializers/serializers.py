from dataclasses import field, fields
from rest_framework import serializers
from community.model.poststorymodels import Posts
from community.model.Eventsmodels import Events
from django.contrib.auth.models import User
# from headrun_community.user.models.models import Profile, Posts

        
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model= Posts
        fields= ['id', 'post_type','posted_username', 'description', 'tags' , 'links', 'created_at', 'updated_at']


class EventSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('user_name')
    class Meta:
        model= Events
        fields= ['id', 'user','event_title', 'event_descript', 'location' , 'team']
        
    def user_name(self,instance):
        print("self", instance.posted_username)
        try:
            return str(instance.posted_username)
        except:
            return 0