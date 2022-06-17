
from django.contrib import admin
from community.models.poststorymodels import FileType, Posts,Reactions,Comments
from community.models.Eventsmodels import Events,EventPhotos,Feedback
# Register your models here.

admin.site.register(Posts)
admin.site.register(FileType)
admin.site.register(Reactions)
admin.site.register(Comments)
admin.site.register(Feedback)
admin.site.register(Events)
admin.site.register(EventPhotos)