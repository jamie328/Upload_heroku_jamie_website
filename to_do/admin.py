from django.contrib import admin
from to_do.models import do_list  # 引入 do_list 這個class
# 後臺管理相關

# 自定義模型管理類
class do_list_admin(admin.ModelAdmin):
	''' member 返回輸出管理類 '''
	list_display = ['event_date','item','priority','completed']  # 顯示會員哪些資料
	list_filter = ('priority','completed')  # filter 按鈕
	search_fields = ('item',)
	ordering = ('priority',)
admin.site.register(do_list,do_list_admin) # 註冊
# Register your models here

# Register your models here.
