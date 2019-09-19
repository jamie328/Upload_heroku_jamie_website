from django.contrib import admin
from myapp.models import member,articles # 引入member class & articles
# 後臺管理相關

# 自定義模型管理類
class member_admin(admin.ModelAdmin):
	''' member 返回輸出管理類 '''
	list_display = ['id','Name','Sex','Birthday']  # 顯示會員哪些資料
	list_filter = ('Name','Sex')  # filter 按鈕
	search_fields = ('Name',)
	ordering = ('id',)
# Register your models here.
# 9/19 新增
class articles_admin(admin.ModelAdmin):
	list_display = ['Title','Create_date']  # 顯示文章資料
	search_fields = ('Title',)
admin.site.register(member,member_admin) # 註冊
admin.site.register(articles,articles_admin) # 註冊文章
