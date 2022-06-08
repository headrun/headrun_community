
from django.contrib import admin
from community.model.poststorymodels import Posts,Reactions,Comments
from community.model.Eventsmodels import Events,EventPhotos,Feedback
# Register your models here.

admin.site.register(Posts)
admin.site.register(Reactions)
admin.site.register(Comments)
admin.site.register(Feedback)
admin.site.register(Events)
admin.site.register(EventPhotos)