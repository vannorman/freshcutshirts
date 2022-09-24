from django.urls import re_path
import fresh_cut_shirts.views

urlpatterns = [
    # Examples:
    # re_path(r'^$', 'fresh_cut_shirts.views.home', name='home'),
    # re_path(r'^blog/', include('blog.re_paths')),



	re_path(r'^$', fresh_cut_shirts.views.home),
        re_path(r'^md/$', fresh_cut_shirts.views.render_md_blog),
	re_path(r'^blog/$', fresh_cut_shirts.views.blog_base), 
	re_path(r'^base/$', fresh_cut_shirts.views.simple_page('base.html')), 
	re_path(r'^resume/$', fresh_cut_shirts.views.simple_page('resume.html')), 
	re_path(r'^portfolio/$', fresh_cut_shirts.views.simple_page('portfolio.html')), 
	re_path(r'^address/$', fresh_cut_shirts.views.simple_page('address.html')), 
	re_path(r'^blog/(.*)$', fresh_cut_shirts.views.blog), 
	re_path(r'^test/$', fresh_cut_shirts.views.test), 
	re_path(r'^jammer/$', fresh_cut_shirts.views.jammer), 
	re_path(r'^messages/whatyouwant$', fresh_cut_shirts.views.simple_page('messages/isthiswhatyouwant.html')), 

]
