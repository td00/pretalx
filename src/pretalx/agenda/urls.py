from django.conf.urls import include, url

from .views import (
    api, schedule, speaker, location
)

agenda_urls = [
    url('^(P<event>\w+)$', schedule.ScheduleView.as_view(), name='schedule'),
    url('^(P<event>\w+)location/$', location.LocationView.as_view(), name='location'),
    url('^(P<event>\w+)talk/(?P<pk>[0-9]+)/$', schedule.TalkView.as_view(), name='talk'),
    url('^(P<event>\w+)speaker/(?P<name>\w+)/$', speaker.SpeakerView.as_view(), name='speaker'),
    url('^(P<event>\w+)api/schedule.xml$', api.FrabView.as_view(), name='frab'),
]
