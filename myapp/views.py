from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import loader, RequestContext # 其實 render就已經封裝好了
from myapp.models import member  # 引入models內的member
# 顯示介面要輸出之文字
# 1.定義Views函數, HttpResponse
# 2.進行urls配置，建立url地址和views的對應關係
# 3.產生html內容
# 4.返回html給browser
def index(request):
    # from myapp.compute import compare
    return render(request, 'myapp/index.html', locals(),)
def about(request):
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
# Create your views here.
