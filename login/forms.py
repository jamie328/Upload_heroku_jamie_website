from django.contrib.auth.forms import UserCreationForm   # 繼承此表單功能
from django.contrib.auth.models import User  # 導入user

class myuser_create_form(UserCreationForm):     # 繼承django內建表單

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')
