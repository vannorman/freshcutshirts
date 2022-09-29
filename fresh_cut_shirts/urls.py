from django.urls import re_path
import fresh_cut_shirts.views

urlpatterns = [
    # Examples:
    # re_path(r'^$', 'fresh_cut_shirts.views.home', name='home'),
    # re_path(r'^blog/', include('blog.re_paths')),



	re_path(r'^$', fresh_cut_shirts.views.home),
	re_path(r'^base/$', fresh_cut_shirts.views.simple_page('base.html')), 
]
