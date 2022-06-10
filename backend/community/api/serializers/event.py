from base.api.serializers import BaseDetailSerializer, BaseModelSerializer

from ...models.Eventsmodels import Events, EventPhotos


class EventsDetailSerializer(BaseDetailSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = Events
        fields = ['posted_username', 'event_title', 'event_descript', 'event_date', 'location', 'team']


class EventPhotosDetailSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = EventPhotos
        fields = ['event_id', 'eventfile_type', 'event_file']
