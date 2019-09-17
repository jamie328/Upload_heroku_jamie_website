from django import forms  # 引入forms功能
from .models import do_list  # 引入do_list

class listform(forms.ModelForm):
	class Meta:
		model = do_list
		# fields = ['item']
		# fields = ['item','priority']
		# fields = ['event_date','item','priority','completed']
		sel_val = (('***','Very important'),('**','Major'),('*','minor'))
		sel_type = forms.CharField(widget= forms.Select(choices= sel_val))
		fields = ['item','priority']