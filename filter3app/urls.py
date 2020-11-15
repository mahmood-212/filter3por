from django.conf.urls import url
from filter3app import views

app_name = 'Read'

urlpatterns=[
    url(r'^index/$',views.index,name='index'),
    url(r'^other/$',views.other,name='other'),
    url(r'^relative/$',views.relative_url,name='relative'),

]