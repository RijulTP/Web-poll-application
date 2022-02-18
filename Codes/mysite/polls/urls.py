from django.urls import path,re_path

from . import views

app_name = 'polls'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('index.html', views.IndexView.as_view(), name='index'),
    path('Detail.html',views.DetailPageView.as_view(), name='detail'),
    path('Votepage.html',views.VotePageView.as_view(), name='votepage'),
    path('CreatePage.html',views.CreatePageView.as_view(), name='createpage'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detailone'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # /polls/post
    path('POST/',views.POST,name='POST'),
    # /polls/GET
    path('GET/',views.GET,name='GET'),
    #/polls/GET/?tags=tag1,tag2
    path(r'^GET/(?P<tags>\[w]+)/$', views.GET,name='GET'),
    #/polls/GET/1
    path('GET/<int:id>/',views.GET,name='GET'),
    #/polls/get/tags/
    path('GET/tags/',views.GET_tags,name='GET'),
    #/polls/PUT/1
    path('PUT/<int:question_id>',views.PUT,name='PUT'),

    
]

#/polls/get/?tags=tag1,tag2
# path('GET/<tags>', views.GETparams,name="GETparams"),
#/polls/put/<id>