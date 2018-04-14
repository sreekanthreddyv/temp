from django.conf.urls import url
from .views import base_view, audio_view, display_view, video_view

urlpatterns = [
    url(r'^$', base_view),
    url(r'audio/', audio_view, name='audio'),
    url(r'display/', display_view, name='display'),
    url(r'video/', video_view, name='video'),
]
