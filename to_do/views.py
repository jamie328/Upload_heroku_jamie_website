from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import loader, RequestContext # 其實 render就已經封裝好了
from to_do.models import do_list  # 引入models內的member
from to_do.forms import listform  # 引入list_form 作為表單回應
from django.contrib import messages # 引入訊息模組
from myapp.models import visit_num
from django.contrib.auth.decorators import login_required  # 只有login才能出現的網頁 否則不能造訪
# 顯示介面要輸出之文字
# 1.定義Views函數, HttpResponse
# 2.進行urls配置，建立url地址和views的對應關係
# 3.產生html內容
# 4.返回html給browser

def to_do_app(request):  # to-do-app
	count_num = visit_num.objects.get(id=3)
	if request.method == "POST":  # 如果 有list要新增 就加入
		# 9/26 新增要有 login required 才能使用新增功能
		if request.user.is_authenticated:
			form = listform(request.POST or None)
			if form.is_valid():
				form.save()
				all_items = do_list.objects.all()
				messages.success(request, "已成功新增 Item 於 To-do-app!!!")
				return render(request, 'to_do/to_do_app.html', locals())
		else:
			return redirect('/login')
	else:
		all_items = do_list.objects.all()
		return render(request, 'to_do/to_do_app.html', locals())

@login_required
def delete(request, item_id):  # 刪除項目
	del_item = do_list.objects.get(id = item_id)
	del_item.delete()
	messages.success(request,"此 Item 已被刪除!!!")
	return redirect('/to_do_app')
@login_required
def completed(request, item_id): # 已完成的 item 要做的事情
	done_item = do_list.objects.get(id = item_id)
	done_item.completed = True
	done_item.save()
	return redirect('/to_do_app')
@login_required
def uncompleted(request, item_id): # 已完成的 item 要做的事情
	done_item = do_list.objects.get(id = item_id)
	done_item.completed = False
	done_item.save()
	return redirect('/to_do_app')
@login_required
def edit(request, item_id):  # edit
	if request.method == "POST":  # 如果 有list要新增 就加入
		edit_item = do_list.objects.get(id =item_id)
		form = listform(request.POST or None, instance=edit_item)
		if form.is_valid():
			form.save()
			messages.success(request, ("已成功編輯此 Item 事件 於 To-do-app!!!"))
		return redirect('/to_do_app')

	else: # 因為按修改，網頁不會是 get
		edit_item = do_list.objects.get(id = item_id)
		return render(request, 'to_do/edit.html', locals())
@login_required
def edit_pri(request, item_id):  # edit_pri
	if request.method == "POST":  # 如果 有list要新增 就加入
		edit_item = do_list.objects.get(id =item_id)
		form = listform(request.POST or None, instance=edit_item)
		if form.is_valid():
			form.save()
			messages.success(request, ("已成功編輯此 Item priority 於 To-do-app!!!"))
		return redirect('/to_do_app')

	else: # 因為按修改，網頁不會是 get
		edit_item = do_list.objects.get(id = item_id)
		return render(request, 'to_do/edit_pri.html', locals())
# Create your views here.
