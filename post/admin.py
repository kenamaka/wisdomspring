from django.contrib import admin
from .models import posts, users , events, comments,userapply

# Register your models here.
admin.site.register(posts)
admin.site.register(users)
admin.site.register(events)
admin.site.register(comments)
admin.site.register(userapply)

