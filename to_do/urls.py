from django.conf.urls import url #新增
from to_do import views

# myapps 應用底下的urls (地方)
# 嚴格匹配開頭結尾

urlpatterns = [
	url(r'^to_do_app/$', views.to_do_app, name='to_do_app'),  # to_do 首頁
	url(r'^to_do_app/delete/(\d+)/$',views.delete),  # 刪除項目
	url(r'^to_do_app/completed/(\d+)/$', views.completed),  # 記錄此項目已完成
	url(r'^to_do_app/uncompleted/(\d+)/$', views.uncompleted),  # 記錄此項目未完成
	url(r'^to_do_app/edit/(\d+)/$', views.edit),  # 記錄此項目導至修改的網頁
	url(r'^to_do_app/edit_pri/(\d+)/$', views.edit_pri)  # 導至edit_pri
]
