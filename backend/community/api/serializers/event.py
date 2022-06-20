from datetime import datetime
from base.api.serializers import BaseDetailSerializer, BaseListCreateSerializer, BaseModelSerializer
from community.models.poststorymodels import Comments, FileType, Posts, Reactions
from rest_framework import serializers
from ...models.Eventsmodels import EventReactions, Events, EventPhotos, Feedback


class EventsDetailSerializer(BaseDetailSerializer):
    event_details = serializers.SerializerMethodField()

    class Meta(BaseDetailSerializer.Meta):
        model = Events
        fields = ['id', 'posted_username', 'event_title', 'event_category',
                  'event_date', 'event_descript', 'location', 'team', 'event_details']

    def get_event_details(self, instance):
        return [(EventPhotosDetailSerializer(m).data for m in instance.event_user.all()),
                (FeadbackDetailSerializer(m).data for m in instance.event_feedbackid.all()),
                (EventReactionsDetailSerializer(m).data for m in instance.event_posted.all())
                ]


class EventPhotosDetailSerializer(BaseListCreateSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = EventPhotos
        fields = ['event_id', 'eventfile_type', 'event_file']


class FeadbackDetailSerializer(BaseListCreateSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = Feedback
        fields = ['event_id', 'event_comment', 'given_by']


class EventReactionsDetailSerializer(BaseListCreateSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = EventReactions
        fields = ['posted_event', 'event_reaction', 'reacted_user']


class PostsDetailSerializer(BaseListCreateSerializer):
    post_details = serializers.SerializerMethodField()

    class Meta(BaseDetailSerializer.Meta):
        model = Posts
        fields = ['id','post_type', 'posted_username', 'date_posted', 'description',
                  'tags', 'links', 'post_details']

    def get_post_details(self, instance):
        return [
                (FileTypeDetailSerializer(m).data for m in instance.postid.all()),
                (CommentsDetailSerializer(m).data for m in instance.post_id.all()),
                (ReactionsDetailSerializer(m).data for m in instance.likedpost.all())
                ]


class PostTypeDetailSerializer(BaseDetailSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = Posts
        fields = ['id','post_type', 'posted_username', 'date_posted', 'description',
                  'tags', 'links']
  

class FileTypeDetailSerializer(BaseDetailSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = FileType
        fields = ['id', 'file_type', 'post_file']


class CommentsDetailSerializer(BaseListCreateSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = Comments
        fields = ['comment_by', 'comment', 'comment_date']


class ReactionsDetailSerializer(BaseDetailSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = Reactions
        fields = ['user', 'reacted_to', 'reaction']


# # feed page/getting all posts
# class AllPostDetailSerializer(BaseDetailSerializer):
#     posts_details = serializers.SerializerMethodField('get_posts_details')

#     class Meta(BaseDetailSerializer.Meta):
#         model = Posts

#     def get_posts_details(self, instance):
#         return [FileTypeDetailSerializer(a).data for a in instance.postid.filter(post_type='POST')]
    

# class PostsEventsSerializer(BaseDetailSerializer):
#         home_postsevents=serializers.SerializerMethodField()
        

#Story/getting stories which are within 24 hrs
class StoriesDetailSerializer(BaseListCreateSerializer):
    stories_details = serializers.SerializerMethodField()

    class Meta(BaseDetailSerializer.Meta):
       model = Posts
       fields = ['id','post_type', 'posted_username', 'date_posted', 'description',
                  'tags', 'links', 'stories_details']
    
    def get_stories_details(self, instance):
        #return [PostsDetailSerializer(a).data for a in instance.createdby.filter(post_type='STORY', , date_posted___lte=datetime.timedelta(hours = 24))]
        return [PostTypeDetailSerializer(a).data for a in instance.postid.filter(file_type="Video")]