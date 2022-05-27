from django.urls import re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
    url(r'^category/(?P<category>\w+)/', views.image_category, name='category'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
