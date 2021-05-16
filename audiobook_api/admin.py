from django.contrib import admin
from audiobook_api import models
# Register your models here.


admin.site.register(models.UserProfile)
# admin.site.register(models.ProfileFeedItem)
admin.site.register(models.SongItem)
admin.site.register(models.PodcastItem)
admin.site.register(models.AudioBookItem)
