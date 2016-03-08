from django.conf.urls import url

urlpatterns = [
    url(r'^all/$', 'login.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'login.views.article'),
    url(r'^language/(?P<language>[a-z\-]+)/$', 'login.views.language'),
    url(r'^create/$', 'login.views.create'),
    url(r'^all/$', 'login.views.articles'),
    url(r'^like/(?P<article_id>\d+)/$', 'login.views.like_article'),
    #url(r'^add_comment/(?P<article_id>\d+)/$', 'login.views.add_comment'),
   # url(r'^delete_comment/(?P<article_id>\d+)/$', 'login.views.delete_comment'),

]
