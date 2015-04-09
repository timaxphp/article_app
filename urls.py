from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
					# Examples:
					# url(r'^$', 'apps.views.home', name='home'),
					# url(r'^blog/', include('blog.urls')),
					url(r'^articles/all/$', 'article.views.articles'),
					url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
					url(r'^articles/addlike/(?P<article_id>\d+)/$', 'article.views.addlike'),
					url(r'^', 'article.views.articles'),

)

