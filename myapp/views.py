from django.shortcuts import render,redirect, get_object_or_404 # 9/25引入404
from django.http import HttpResponse
from datetime import datetime
from django.template import loader, RequestContext # 其實 render就已經封裝好了
from myapp.models import member,articles,visit_num  # 引入models內的member
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # 顯示頁數
from django.db.models import Q  # 使用 OR and 等
# 顯示介面要輸出之文字
# 1.定義Views函數, HttpResponse
# 2.進行urls配置，建立url地址和views的對應關係
# 3.產生html內容
# 4.返回html給browser
def index(request):
    # from myapp.compute import compare
    articles_all = articles.objects.all()  # .order_by('-Create_date')
    count_num = visit_num.objects.get(id = 3)  # 創建跑去id=3 第一次取確認有無取到
    if count_num: #有取到值
        count_num.count += 1
        count_num.save()
    # 9/24 新增分頁系統
    paginator = Paginator(articles_all, 3) # 每一頁只顯示 3個 把文章切割
    page = request.GET.get('page') # 獲得當前頁碼
    try:
        posts = paginator.page(page) # ()內的為某頁的紀錄 當前頁數
    except PageNotAnInteger: # 不是整數
        posts = paginator.page(1)  # 剛開始進去為第1頁
    except EmptyPage:  # 頁數超過最後一頁顯示最後一頁
        posts = paginator.page(paginator.num_pages)  # 總共頁數的最後一頁
    return render(request, 'myapp/index.html', locals(),)
def about(request):
    count_num = visit_num.objects.get(id=3)
    return render(request, 'myapp/about.html', locals(),)
# def index_image(request, username):
#     now = datetime.now()
#     test_text = 'Yoyoman!!!!'
#     list_num = list(range(1,11))
#     return render(request, 'myapp/index_image.html', locals()) # 導至index_image.html
def member_index(request): # member 主頁
    members_all = member.objects.all()
    return render(request, 'myapp/member_index.html', locals()) # 呼叫html模板
def member_detail(request, mid):
    """給出會員訊息"""
    # 拿到各別會員資訊
    member_info = member.objects.get(id = mid)
    return render(request, 'myapp/member_detail.html', locals()) # 呼叫html模板
def create(request):
    ''' 創立一個項目 '''
    # 1.創立一個 class 項目
    member_new = member()
    member_new.Name = '新增測試名'
    # 2.存檔
    member_new.save()
    # 3.返回模板或是定向為訪問其他
    return redirect('/member_index')
def delete(request, mid):
    # 1. 取得要刪除的項目
    member_del = member.objects.get(id = mid)
    member_del.delete()
    return redirect('/member_index')
def search(request):
    count_num = visit_num.objects.get(id = 3)  # 創建跑去id=3 第一次取確認有無取到
    query = request.GET.get('q')
    results = articles.objects.all().filter(Q(Title__contains=str(query)) | (Q(Intro__contains=str(query))))
    # if results is None:
    #     not_found = '你搜尋的關鍵字:' + str(query) + '，在部落格找不到相關結果！！'
    # 9/24 新增分頁系統
    paginator = Paginator(results, 3)  # 每一頁只顯示 3個 把文章切割
    page = request.GET.get('page')  # 獲得當前頁碼
    try:
        posts = paginator.page(page)  # ()內的為某頁的紀錄 當前頁數
    except PageNotAnInteger:  # 不是整數
        posts = paginator.page(1)  # 剛開始進去為第1頁
    except EmptyPage:  # 頁數超過最後一頁顯示最後一頁
        posts = paginator.page(paginator.num_pages)  # 總共頁數的最後一頁
    return render(request, 'myapp/search.html', locals()) # 呼叫search模板

def website_log(request):
    count_num = visit_num.objects.get(id=3)
    templates = 'myapp/website_log.html'
    return render(request, templates, locals(),)
# Create your views here.
