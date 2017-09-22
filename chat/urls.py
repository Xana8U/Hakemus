from django.conf.urls import url

from . import views


app_name = 'chat'
urlpatterns = [
    # ex: /polls/  < r'^ = polls root, $ = url finisher, (?P<>[]) = url number generation by ID in array
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^messages/$', views.SendView.as_view(), name='send'),
    url(r'^log/$', views.LogView.as_view(), name='log'),
    url(r'^add/$', views.add, name='add'),

]
