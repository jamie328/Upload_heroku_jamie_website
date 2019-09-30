from django.db import models
from datetime import date  # 9/15更改
from django.utils import timezone
from django.contrib.auth.models import User  # 導入user

class bbs(models.Model):  # 為單一類
	postman = models.CharField(max_length =25, default='訪客')
	post_choice = (('分享', 'share'),('心情', 'mood'), ('爆卦', 'gossip'), ('請益', 'question'))
	post_type = models.CharField(max_length=30, choices=post_choice, default='share')
	post_title = models.CharField(max_length=30, null=False, default=' ')
	post_date = models.DateTimeField(null=False, default=timezone.now())
	post_content = models.TextField(blank=True)
	# 主要為 讚、噓、留言(多類) 讚跟噓訪客可以點
	post_likes = models.IntegerField(default=0)
	post_hates = models.IntegerField(default=0)

	def __str__(self):
		# 返回字串
		return str(self.post_title)
	class Meta:
		db_table = 'bbs'
		ordering = ('-post_date',)  # 9/29 寫在 models Meta內以降序排列
	def likes(self):  # 案讚+1
		self.post_likes += 1
		self.save(update_fields=['post_likes'])
	def hates(self):
		self.post_hates +=1
		self.save(update_fields=['post_hates'])
# 留言為多類
class bbs_comment(models.Model):
	#  留言只有註冊的人
	comment_post = models.ForeignKey('bbs', on_delete=models.CASCADE)  # 一篇文章下有多個評論
	comment_content = models.CharField(max_length=150, null=False)
	# comment_num = models.IntegerField(default=0) # 應該是不需要
	comment_man = models.CharField(max_length=25, default="訪客")
	comment_date = models.DateTimeField(null=False, default=timezone.now())
	def __str__(self):
		# 返回字串
		return str(self.comment_post)
	class Meta:
		db_table = 'bbs_comment'
		ordering = ('-comment_date',)  # 9/29 寫在 models Meta內以降序排列
