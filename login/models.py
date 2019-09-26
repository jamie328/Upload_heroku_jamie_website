from django.db import models
# from datetime import date  # 9/15更改
from django.utils import timezone

# class do_list(models.Model):
# 	item = models.CharField(max_length=100, null=False,default="None Item")
# 	priority_choice = (('***','Very important'),('**','Major'),('*','minor'))
# 	priority = models.CharField(max_length = 20, choices= priority_choice, default="*")
# 	completed = models.BooleanField(default=False)
# 	event_date = models.DateField(null=False,default=timezone.now())
# 	# event_date = models.DateField(null=False,default=date.today())
# 	def __str__(self):
# 		# 返回字串
# 		return str(self.event_date) + self.item + self.priority
# 	class Meta:
# 		db_table = 'do_list'
# Create your models here.
