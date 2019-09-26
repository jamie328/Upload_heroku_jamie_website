from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
# from django.template import loader, RequestContext # 其實 render就已經封裝好了
# from to_do.models import do_list  # 引入models內的member
# from to_do.forms import listform # 引入list_form 作為表單回應
from django.contrib import messages # 引入訊息模組
from myapp.models import visit_num # 瀏覽人數
from django.contrib.auth import authenticate, login, logout # 引入django 內建的 login
from django.contrib.auth.decorators import login_required  # 只有login才能出現的網頁 否則不能造訪
from .forms import myuser_create_form  # 繼承django內建的UserCreationForm
from django.contrib.auth.models import User  # 導入user
from django.contrib.auth.forms import UserCreationForm   # 繼承此表單功能


@login_required
def dashboard(request):  # 登入成功頁面 訪問網址  /login/successful/
	count_num = visit_num.objects.get(id=3)
	username = request.user.first_name
	templates = 'login/dashboard.html'
	return render(request, templates, locals())
def registration(request):
	count_num = visit_num.objects.get(id=3)
	if request.method == 'POST':  # 如果是要傳回值
		user_form = myuser_create_form(request.POST or None)  # 確認 user_form 是 POST
		if user_form.is_valid():  # 確認都是有效的
			new_user = user_form.save(commit=False)
			new_user.set_password(
				user_form.cleaned_data['password1']   # 設置密碼以表單上的password1
			)
			new_user.save()
			templates = 'login/register_done.html'
			return render(request, templates, locals())
		else:
			# 可能要想一下如何模組化
			user_form = myuser_create_form()
			templates = 'login/registration.html'
			if UserCreationForm.error_messages:
				error_msg = UserCreationForm.error_messages
			return render(request, templates, locals(),)
	else:
		# 如果是GET 就代表使用者單純填入表單
		templates = 'login/registration.html'
		user_form = myuser_create_form()
		templates = 'login/registration.html'
		return render(request, templates, locals(),)
