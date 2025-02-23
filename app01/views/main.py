from django.shortcuts import render, redirect

from app01 import models
from app01.utils.pagination import Pagination


def search(request):
    info_dict = request.session['info']
    if request.method == 'GET':
        return render(request, "search.html")
    text = request.POST.get('wd')
    user_id = info_dict['id']
    print(text)
    models.History.objects.create(text=text, user_id=user_id)
    return redirect("https://www.baidu.com/s?wd={}".format(text))


def history(request):
    """搜索历史"""
    # 检查是否登录
    info_dict = request.session['info']

    # 根据输入查询
    data_dict = {'user': info_dict['id']}  # 查询条件,首先明确用户
    search_data = request.GET.get("q", "")  # 获取搜索条件，"" 表示默认为空字符串
    if search_data:
        data_dict["text__contains"] = search_data
    queryset = models.History.objects.filter(**data_dict).order_by("id")

    # 页码器
    page_object = Pagination(request, queryset)

    # 传入参数
    context = {
        'queryset': queryset,
        'page_string': page_object.html(),
        'user_name': info_dict.get('user_name'),
    }
    return render(request, "history.html", context)


def history_delete(request, nid):
    models.History.objects.filter(id=nid).delete()
    return redirect("/main/history/", {"queryset": models.History.objects.order_by("id")})
