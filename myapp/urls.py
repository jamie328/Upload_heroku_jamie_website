from django.conf.urls import url #新增
from myapp import views

# myapps 應用底下的urls (地方)
# 嚴格匹配開頭結尾

urlpatterns = [
    url(r'^index/$', views.index, name='index'),  # 地方urls 進行匹配，正則須為index結尾
	url(r'^about/$', views.about, name = 'about'),
	# url(r'^index_image/(\w+)/$', views.index_image), #地方urls 匹配至views.index_image
	url(r'^member_index/$', views.member_index, name='member_index'), #地方urls匹配member_index
	url(r'^members/(\d+)/$', views.member_detail, name='member_detail'), #地方urls匹配member_detail
	url(r'^create/$',views.create), # 創建
	url(r'^delete(\d+)/', views.delete), #刪除
	url(r'^search', views.search, name='search'), # 9/24 完成
	url(r'^website_log', views.website_log, name='website_log'),  # 9/26新增
]
