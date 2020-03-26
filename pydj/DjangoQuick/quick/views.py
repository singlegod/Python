# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# HttpResponse表示的是Http的响应
from django.shortcuts import render  # 模板快捷函数
from .models import User

# # 新添加
# def index(request):
#     return HttpResponse('success')
def index(request):
    # 判断是否为post请求
    if request.method == 'POST':
        # 获取到请求参数，username的写法,如果username不存在不会抛出异常
        # password会抛出异常
        username = request.POST.get('username')
        password = request.POST['password']

        u=User(username=username,password=password)
        u.save()
        # 业务 需求: 查询出所有数据
        users = User.objects.all()
        # 返回给用户  模版中使用到的users就是这里传递进去的
        return render(request, template_name='index.html', context={
            'users': users

        })
    return render(request, 'index.html')
