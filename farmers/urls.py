from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^$", views.index, name="index"),
    # url(r"^verify$", views.verify, name="verify"),
    url(r"^whitelist$", views.whitelist, name="whitelist"),
    url(r'^myajaxformview', views.myajaxformview, name='myajaxformview'),
]
