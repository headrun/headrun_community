from datetime import datetime
from base.api.serializers import BaseDetailSerializer, BaseListCreateSerializer, BaseModelSerializer
from community.models.poststorymodels import Comments, FileType, Posts, Reactions
from rest_framework import serializers
from ...models.Eventsmodels import EventReactions, Events, EventPhotos, Feedback


class EventsDetailSerializer(BaseDetailSerializer):
    event_photos = serializers.SerializerMethodField()

    class Meta(BaseDetailSerializer.Meta):
        model = Events
        fields = ['id', 'posted_username', 'event_title', 'event_category',
                  'event_date', 'event_descript', 'location', 'team', 'event_photos']

    def get_event_photos(self, instance):
        return [EventPhotosDetailSerializer(m).data for m in instance.event_user.all()]


class EventPhotosDetailSerializer(BaseListCreateSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = EventPhotos
        fields = ['event_id', 'eventfile_type', 'event_file']


class FeadbackDetailSerializer(BaseDetailSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = Feedback
        fields = ['id', 'event_id', 'feedback', 'given_by']


class EventReactionsDetailSerializer(BaseListCreateSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = EventReactions
        fields = ['id', 'posted_event', 'event_reaction', 'reacted_user']


class PostsDetailSerializer(BaseListCreateSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = Posts
        fields = ['post_type', 'posted_username', 'date_posted', 'description', 'tags', 'links']


class FileTypeDetailSerializer(BaseDetailSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = FileType
        fields = ['id', 'file_type', 'post_file']


class CommentsDetailSerializer(BaseListCreateSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = Comments
        fields = ['comment_by', 'post_id', 'comment', 'comment_date']


class ReactionsDetailSerializer(BaseDetailSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = Reactions
        fields = ['user', 'reacted_to', 'reaction']


# feed page/getting all posts
class AllPostDetailSerializer(BaseDetailSerializer):
    posts_details = serializers.SerializerMethodField('get_posts_details')

    class Meta(BaseDetailSerializer.Meta):
        model = Posts

    def get_posts_details(self, instance):
        return [FileTypeDetailSerializer(a).data for a in instance.postid.all()]
    

class PostsEventsSerializer(BaseDetailSerializer):
        home_postsevents=serializers.SerializerMethodField()
        

#Story/getting stories which are within 24 hrs
class StoriesDetailSerializer(BaseDetailSerializer):
    stories_details = serializers.SerializerMethodField()

    class Meta(BaseDetailSerializer.Meta):
       model = Posts

    def get_stories_details(self, instance):
        #return [PostsDetailSerializer(a).data for a in instance.createdby.filter(post_type='STORY', date_posted___lte=datetime.hour(24))]
        return [PostsDetailSerializer(a).data for a in instance.post_type.filter(post_type='STORY')]