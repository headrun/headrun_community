from datetime import timezone
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from base.models import BaseActiveOrderedModel,BaseActiveModel
# Create your models here.
TEAM_CHOICES=(
    ("HRH","HRH"),
    ("HRB","HRB"),
)
EVENTFILE_CHOICES=(
    ("PHOTO","PHOTO"),
    ("VIDEO","VIDEO"),
    ("AUDIO","AUDIO"),
)

class Events(BaseActiveOrderedModel):
    posted_username=models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name="event_postedby")
    event_title=models.CharField(max_length=50, null=True)
    event_descript=models.TextField(max_length=500, null=True)
    event_date=models.DateTimeField(default = timezone.now)
    location=models.CharField(max_length=500)
    team=models.CharField(max_length=20, choices = TEAM_CHOICES,default="HRH")
        
    def __str__(self):
        return self.event_title
    
class EventPhotos(BaseActiveOrderedModel):
    event_id=models.ForeignKey(Events,on_delete=models.CASCADE,null=True, related_name="event_user")
    eventfile_type=models.CharField(max_length=20, choices = EVENTFILE_CHOICES,default="PHOTO")
    event_file=models.FileField(upload_to='static/', null=True, verbose_name="event_images")
    
class Feedback(BaseActiveOrderedModel):
    event_id=models.ForeignKey(Events,on_delete=models.CASCADE,null=True, related_name="post_feedbackid")
    feedback=models.TextField(max_length=500 , null=True)
    given_by= models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name="given_user")
    
    