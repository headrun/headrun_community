from base.api.serializers import BaseDetailSerializer, BaseModelSerializer

from ...models.Eventsmodels import Events, EventPhotos


class EventsDetailSerializer(BaseDetailSerializer):
    class Meta(BaseDetailSerializer.Meta):
        model = Events


class EventPhotosDetailSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = EventPhotos
