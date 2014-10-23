from django.conf.urls import url
from psec.an_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]