from django.db import models
from datetime import datetime
from datetime import date
from django.utils import timezone

# 設計和資料庫表對應的類

class member(models.Model):
	Name = models.CharField(max_length=20, null=False)
	sex_choice = (('Male', 'Male'), ('Female', 'Female'))
	Sex = models.CharField(max_length=10, choices=sex_choice, default='Male')
	Birthday = models.DateField(null=False, default=date(1990, 1, 20))
	Phone = models.CharField(max_length=50, default='09XXXXXXXX')
	def __str__(self):
		# 返回字串
		return self.Name
	class Meta:
		db_table = 'mem'
# 9/19 新增 文章列表
class articles(models.Model):
	Title = models.CharField(max_length=50, null=False)
	Image = models.CharField(max_length=50, null=False)
	Intro = models.TextField()
	Href = models.CharField(max_length=80, null=False)
	Create_date = models.DateField(null=False, default=timezone.now())
	# Create_date = models.DateField(null=False, default=date.today())
	def __str__(self):
		# 返回字串
		return self.Title
	class Meta:
		db_table = 'articles'  # 9/24 在資料庫內改名
		ordering = ('-Create_date',)  # 9/24 寫在 models Meta內以降序排列
# Create your models here.

# 9/19 新增網站瀏覽次數
class visit_num(models.Model):
	count = models.PositiveIntegerField(default=0)
	def __str__(self):
		return str(self.count)
	class Meta:
		db_table = 'visit_num'