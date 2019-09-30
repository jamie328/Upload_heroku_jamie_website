from django.urls import path
from django.conf.urls import url #新增
from . import views  # import bbs 的 views

# myapps 應用底下的urls (地方)
# 嚴格匹配開頭結尾
# 因採用django 內建的auth_views 因此不用再呼叫到login 的 views ，只需填妥template

urlpatterns = [
	# url(r'^login/$', views.login, name='login'),  # 給模板呼叫 login url 並對應views的login
	  url(r'^bbs/$', views.bbs_index, name='bbs_index'),
	  url(r'^bbs/bbs_new_articles/$', views.bbs_new_articles, name='bbs_new_articles'),
	  url(r'^bbs_likes_post/(?P<post_id>\d+)/', views.bbs_likes_post, name='bbs_likes_post'),
	  url(r'^bbs_hates_post/(?P<post_id>\d+)/', views.bbs_hates_post, name='bbs_hates_post'),
	  url(r'^bbs_new_comment/(?P<post_id>\d+)/', views.bbs_new_comment, name='bbs_new_comment'),
	  url(r'^bbs_revise_articles/(?P<post_id>\d+)/', views.bbs_revise_articles, name='bbs_revise_articles'),
	url(r'^bbs_delete_articles/(?P<post_id>\d+)/', views.bbs_delete_articles, name='bbs_delete_articles'),
]