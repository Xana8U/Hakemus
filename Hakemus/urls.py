from django.conf.urls import url

from . import views


app_name = 'Hakemus'
urlpatterns = [
    # ex: /hakemus/  < r'^ = polls root, $ = url finisher, (?P<>[]) = url number generation by ID in array
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^questions', views.QuestionsView.as_view(), name='questions'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
