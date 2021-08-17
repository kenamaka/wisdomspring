
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path ("", views.index, name= 'index'),
    path ('admin/', admin.site.urls),
    path("<str:post_title>/post", views.postpage, name = "postpage"),
    path("<str:event_title>/event",views.eventfull, name ="event"),
    path("events/", views.eventpage, name = "events"),
    path("login/", views.login_view, name = "login"),
    path("admission/", views.admission, name = "admission"),
    path("prospects/", views.prospects, name = "prospects"),
    path("contact/", views.contact, name = "contact"),
    path("blogs/", views.blogpage, name = "blogpage"),
    path("apply/", views.apply, name = "apply"),
    path("administrator/",views.administrator, name = "administrator"),
    path("administrator/upload_post/", views.upload_post, name = "upload_post"),
    path("administrator/upload_event/", views.upload_event, name = "upload_event"),
    path("administrator/add_comment/", views.add_comment, name = "add_comment"),
    path("administrator/add_user/", views.add_user, name = "add_user"),
    path("administrator/post_list/", views.post_list, name = "post_list"),
    path("administrator/event_list/", views.event_list, name = "event_list"),
    path("administrator/user_list/", views.user_list, name = "user_list"),
    path("administrator/comment_list/", views.comment_list, name = "comment_list"),
    path("apply/", views.apply_user, name = "apply"),
    
    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
