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


# 9/19 新增 文章列表
class articles(models.Model):
	Title = models.CharField(max_length=50, null=False)
	Image = models.CharField(max_length=50, null=False)
	Intro = models.TextField()
	Href = models.CharField(max_length=80, null=False)
	Create_date = models.DateField(null=False, default=timezone.now())
	def __str__(self):
		# 返回字串
		return self.Title
# Create your models here.
