from django import forms  # 引入forms功能
from .models import bbs, bbs_comment  # 引入 model 模組

class bbs_form(forms.ModelForm):
	# postman = forms.CharField(label='發文者',max_length=30)
	post_choice = (('分享', 'share'), ('心情', 'mood'), ('爆卦', 'gossip'), ('請益', 'question'))
	post_type = forms.CharField(label='發文類型', widget=forms.Select(choices=post_choice))
	post_title = forms.CharField(label='標題', max_length=30, widget=forms.TextInput)
	# post_date 也是當下時間
	post_content = forms.CharField(label='內容', widget=forms.Textarea)
	# post_likes and post_hates 預設為 0

	class Meta:
		model = bbs
		fields = ['postman', 'post_type', 'post_title', 'post_content']

class bbs_comment_form(forms.ModelForm):
	# 不把 comment_post 寫進去 用 views.py 處理
	class Meta:
		model = bbs_comment
		fields = ['comment_post', 'comment_man', 'comment_content']
