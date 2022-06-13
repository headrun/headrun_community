from base.api.serializers import BaseDetailSerializer, BaseListCreateSerializer, BaseModelSerializer
from community.models.poststorymodels import Comments, FileType, Posts, Reactions

from ...models.Eventsmodels import EventReactions, Events, EventPhotos, Feedback


class EventsDetailSerializer(BaseDetailSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = Events
        fields = ['id', 'posted_username', 'event_title', 'event_descript', 'event_date', 'location', 'team']


class EventPhotosDetailSerializer(BaseDetailSerializer):
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
