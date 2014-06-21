from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

def mypage(req):
	import myproj.mypage
	return myproj.mypage.index(req)

urlpatterns = patterns('',
    # Examples:
    url(r'^mongo', mypage, name='mypage'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
