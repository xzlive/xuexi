from django.conf.urls import url

from . import view

urlpatterns = [
    url(r'^hel', view.hello),
]
