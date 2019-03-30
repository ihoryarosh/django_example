from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index_DV'),
    url(r'about/.+', views.about, name='about_job')
]
