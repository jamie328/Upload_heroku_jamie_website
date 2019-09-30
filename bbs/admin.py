from django.contrib import admin
from bbs.models import bbs, bbs_comment
# 後臺管理相關

class bbs_adimin(admin.ModelAdmin):
	list_display = ['id','postman', 'post_type', 'post_title', 'post_date', 'post_likes']
	list_filter = ('post_likes', 'post_hates')
	ordering = ('-post_date',)   # 按照新的發表到舊的
class bbs_comment_admin(admin.ModelAdmin):
	list_display = ['id', 'comment_post', 'comment_content']
	ordering = ('-comment_date',)   # 按照新的發表到舊的

admin.site.register(bbs, bbs_adimin)
admin.site.register(bbs_comment, bbs_comment_admin)

# # 自定義模型管理類
# class do_list_admin(admin.ModelAdmin):
# 	''' member 返回輸出管理類 '''
# 	list_display = ['event_date','item','priority','completed']  # 顯示會員哪些資料
# 	list_filter = ('priority','completed')  # filter 按鈕
# 	search_fields = ('item',)
# 	ordering = ('priority',)
# admin.site.register(do_list,do_list_admin) # 註冊
# Register your models here

# Register your models here.
