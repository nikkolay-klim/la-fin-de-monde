from django.conf.urls import url

from .views import EntryDetail

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', EntryDetail.as_view(), name='entry_detail'),
]
