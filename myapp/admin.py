from django.contrib import admin
from myapp.models import member # 引入member class
# 後臺管理相關

# 自定義模型管理類
class member_admin(admin.ModelAdmin):
	''' member 返回輸出管理類 '''
	list_display = ['id','Name','Sex','Birthday']  # 顯示會員哪些資料
	list_filter = ('Name','Sex')  # filter 按鈕
	search_fields = ('Name',)
	ordering = ('id',)
# Register your models here.
admin.site.register(member,member_admin) # 註冊
