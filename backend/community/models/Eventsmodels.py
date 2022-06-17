from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from base.models import BaseActiveOrderedModel

# Create your models here.
TEAM_CHOICES = (
    ("HRH", "HRH"),
    ("HRB", "HRB"),
)
EVENTFILE_CHOICES = (
    ("PHOTO", "PHOTO"),
    ("VIDEO", "VIDEO"),
    ("AUDIO", "AUDIO"),
)
CATEGORY_CHOICES = (
    ("R AND R", "R AND R"),
    ("BIRTHDAY", "BIRTHDAY"),
    ("ANNIVERSARY", "ANNIVERSARY"),
)
REACTION_CHOICES = (
    ("INTERESTED", "INTERESTED"),
    ("NOT INTERESTED", "NOT INTERESTED"),
    ("GOING", "GOING"),
)


# Event details Model
class Events(BaseActiveOrderedModel):
    posted_username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="event_postedby")
    event_title = models.CharField(max_length=50, null=True, blank=True)
    event_descript = models.TextField(max_length=500, null=True, blank=True)
    event_category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="R AND R")
    event_date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=500, null=True, blank=True)
    team = models.CharField(max_length=20, choices=TEAM_CHOICES, default="HRH")
    
    def __str__(self):
        return self.event_title
    
    class Meta(BaseActiveOrderedModel.Meta):
        pass


# Event photos,videos or audio files
class EventPhotos(BaseActiveOrderedModel):
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE, related_name="event_user")
    eventfile_type = models.CharField(max_length=20, choices=EVENTFILE_CHOICES, default="PHOTO")
    event_file = models.FileField(upload_to='static/', verbose_name="event_images")

    def __str__(self):
        return self.event_id.event_title
    
    class Meta(BaseActiveOrderedModel.Meta):
        pass


# Feedback on events
class Feedback(BaseActiveOrderedModel):
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE, related_name="event_feedbackid")
    event_comment = models.TextField(max_length=500)
    given_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedback_givenby")

    def __str__(self):
        return self.event_comment
    
    class Meta(BaseActiveOrderedModel.Meta):
        pass


# Event reactions
class EventReactions(models.Model):
    posted_event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name="event_posted")
    event_reaction = models.CharField(max_length=20, choices=REACTION_CHOICES, default="NOT INTERESTED")
    reacted_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="given_user")

    class Meta(BaseActiveOrderedModel.Meta):
        ordering = ["posted_event", "event_reaction", "reacted_user"]
