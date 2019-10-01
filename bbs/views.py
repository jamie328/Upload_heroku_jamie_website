from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
# from django.template import loader, RequestContext # 其實 render就已經封裝好了
from django.contrib import messages # 引入訊息模組
from myapp.models import visit_num  # 瀏覽人數
from .models import bbs, bbs_comment
from django.contrib.auth import authenticate, login, logout # 引入django 內建的 login
from django.contrib.auth.decorators import login_required  # 只有login才能出現的網頁 否則不能造訪
from django.contrib.auth.models import User  # 導入user
from bbs.forms import bbs_form, bbs_comment_form  # 引入自己設計表單
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # 顯示頁數


def bbs_index(request):
	count_num = visit_num.objects.get(id=3)
	count_num.viewed()
	post = bbs.objects.all()
	art_comment = []
	for po in post:
		if po.bbs_comment_set.all():
			art_comment.append(po.bbs_comment_set.all())
		else:
			art_comment.append([])
	my_list = zip(post, art_comment)
	templates = 'bbs/bbs.html'
	# username = User.get_username(request)
	comment_form = bbs_comment_form()
	return render(request, templates, locals(),)


@login_required
def bbs_new_articles(request):
	count_num = visit_num.objects.get(id=3)
	if request.method == 'POST':  # 如果是要傳回值
		post_form = bbs_form(request.POST or None)  # 確認 bbs_form 是 POST
		if post_form.is_valid():
			post_form.save()
			messages.success(request, "已成功新增文章於BBS!!!")
			return redirect('/bbs')
	else:  # 如果是get
		po_man = request.user.first_name
		templates = 'bbs/bbs_new_articles.html'
		post_form = bbs_form()
		return render(request, templates, locals())


def bbs_likes_post(request, post_id):
	post_art = bbs.objects.get(pk=post_id)
	post_art.likes()
	messages.success(request, ("讚起來!!!"))
	return redirect('/bbs')


def bbs_hates_post(request, post_id):
	post_art = bbs.objects.get(pk=post_id)
	post_art.hates()
	messages.success(request, ("噓聲四起!!!"))
	return redirect('/bbs')


def bbs_new_comment(request, post_id):
	count_num = visit_num.objects.get(id=3)
	the_post = bbs.objects.get(pk=post_id)
	if request.method == "POST":
		comment_form = bbs_comment_form(request.POST or None)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.comment_post = the_post
			new_comment.save()
			messages.success(request, "已成功新增留言囉!!!")
			#  下面可以不用加 因為 redirect 就會導到 bbs views
			# post = bbs.objects.all()
			# art_comment = []
			# for po in post:
			# 	if po.bbs_comment_set.all():
			# 		art_comment.append(po.bbs_comment_set.all())
			# 	else:
			# 		art_comment.append([])
			# my_list = zip(post, art_comment)
			# templates = 'bbs/bbs.html'
			# username = User.get_username(request)
			return redirect('/bbs')
		else:
			return redirect('/bbs')


@login_required
def bbs_revise_articles(request, post_id):
	count_num = visit_num.objects.get(id=3)
	the_post = bbs.objects.get(pk=post_id)
	if request.user.first_name == the_post.postman:
		if request.method == 'POST':  # 把修改資料傳回資料庫存 並 回 BBS 頁面
			revise_form = bbs_form(request.POST or None, instance=the_post)
			if revise_form.is_valid():
				revise_form.save()
				messages.success(request, ("已成功修改你發布的 bbs 文章囉!!!"))
			return redirect('/bbs')
		else:  # 給予修改表單
			templates = 'bbs/bbs_revise_articles.html'
			return render(request, templates, locals(),)
	else:
		messages.success(request, ("你不是發布文章的人，不能修改哦！"))
		return redirect('/bbs')


@login_required
def bbs_delete_articles(request, post_id):
	deleted_articles = bbs.objects.get(pk=post_id)
	if request.user.first_name == deleted_articles.postman:
		deleted_articles.delete()
		messages.success(request, "剛剛你選取的文章已被刪除囉!!!")
		return redirect('/bbs')
	else:
		messages.success(request, ("你不是發布文章的人，不能亂刪哦！"))
		return redirect('/bbs')


@login_required()
def bbs_revise_comment(request, comment_id):
	the_comment = bbs_comment.objects.get(pk=comment_id)
	if request.user.first_name == the_comment.comment_man:
		if request.method == 'POST':
			comment_form = bbs_comment_form(request.POST or None, instance=the_comment)
			if comment_form.is_valid():
				comment_form.save()
				messages.success(request, "你已成功修改你的留言哦!!!")
				return redirect('/bbs')
		else:
			templates = 'bbs/bbs_revise_comment.html'
			return render(request, templates, locals(),)
	else:
		messages.success(request, "你不是這個留言的擁有者，不能修改留言哦!!!")
		return redirect('/bbs')


@login_required()
def bbs_delete_comment(request, comment_id):
	count_num = visit_num.objects.get(id=3)
	the_comment = bbs_comment.objects.get(pk=comment_id)
	if request.user.first_name == the_comment.comment_man:
		the_comment.delete()
		messages.success(request, "你點選的流言已刪除囉!!!")
		return redirect('/bbs')
	else:
		messages.success(request, "你不是這個留言的擁有者，不能刪除留言哦!!!")
		return redirect('/bbs')


