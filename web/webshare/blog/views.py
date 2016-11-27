# -*- coding: utf-8 -*-
import logging
import datetime
#import json

from django.shortcuts import render, redirect
#from django.core.urlresolvers import reverse
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

from django.db.models import Count
from blog.models import User,Category,Article,Comment, Tag
from blog.forms import LoginForm,RegForm,CommentForm,ChangepwdForm,AddArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

import blog

#import json

logger = logging.getLogger('blog.views')

# Create your views here.
def global_setting(request):
    # 站点基本信息
    SITE_URL = settings.BLOG_URL
    SITE_NAME = settings.BLOG_NAME
    SITE_DESC = settings.SITE_DESC
    # 分类信息获取（导航数据）
    category_list = Category.objects.all()[:3]
    
    # 文章归档数据
    archive_list = Article.objects.distinct_date()
    # 广告数据（同学们自己完成）
    # 标签云数据（同学们自己完成）
    # 友情链接数据（同学们自己完成）
    # 文章排行榜数据（按浏览量和站长推荐的功能同学们自己完成）
    # 评论排行
    comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
    article_comment_list = [Article.objects.get(pk=comment['article']) for comment in comment_count_list]
    return locals()

def index(request):
    try:
        pass
        # 最新文章数据
        article_list = Article.objects.all()
        article_list = getPage(request, article_list)
        # 文章归档   
        # 1、先要去获取到文章中有的 年份-月份  2015/06文章归档
        # 使用values和distinct去掉重复数据（不可行）
        # print Article.objects.values('date_publish').distinct()
        # 直接执行原生sql呢？
        # 第一种方式（不可行）
        # archive_list =Article.objects.raw('SELECT id, DATE_FORMAT(date_publish, "%%Y-%%m") as col_date FROM blog_article ORDER BY date_publish')
        # for archive in archive_list:
        #     print archive
        # 第二种方式（不推荐）
        # cursor = connection.cursor()
        # cursor.execute("SELECT DISTINCT DATE_FORMAT(date_publish, '%Y-%m') as col_date FROM blog_article ORDER BY date_publish")
        # row = cursor.fetchall()
        # print row
    except Exception as e:
        print e
        logger.error(e)
    return render(request, 'blog/index.html', locals())

def archive(request):
    try:
        # 先获取客户端提交的信息
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        article_list = Article.objects.filter(date_publish__icontains=year+'-'+month)
        article_list = getPage(request, article_list)
    except Exception as e:
        logger.error(e)
    return render(request, 'blog/archive.html', locals())

# 按标签查询对应的文章列表
def tag(request):
    try:
        # 同学们自己实现该功能
        pass
    except Exception as e:
        logger.error(e)
    return render(request, 'blog/archive.html', locals())

# 分页代码,增加分页属性
def getPage(request, article_list):
    paginator = Paginator(article_list, 5)#2个文章进行分页
    page = int(request.GET.get('page', 1))
    try:
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list

# 文章详情页面
def article(request):
    try:
        # 获取文章id
        aid = request.GET.get('id', None)
        try:
            # 获取文章信息
            article = Article.objects.get(pk=aid)
        except Article.DoesNotExist:
            return render(request, 'blog/failure.html', {'reason': '没有找到对应的文章'})

        # 评论表单
        comment_form = CommentForm({'author': request.user.username,
                                    'email': request.user.email,
                                    'url': request.user.url,
                                    'article': aid} if request.user.is_authenticated() else{'article': id})#此处故意写错，不登陆文章id不正确
        # 获取评论信息                                            
        comments = Comment.objects.filter(article=article).order_by('id')
        comment_list = []
        for comment in comments:
             
            for item in comment_list:#前端全部有子评论
                if not hasattr(item, 'children_comment'):#设置子评论属性
                    setattr(item, 'children_comment', [])
                if comment.pid == item:
                    item.children_comment.append(comment)
                    break
            
            if comment.pid is None:#没有父评论
                comment_list.append(comment)
            '''    
            else :#是子评论
                #次次级评论也会出来，父级出现重复
                pcommet=comment.pid                
                if not hasattr(pcommet, 'children_comment'):#设置子评论属性
                    setattr(pcommet, 'children_comment', [comment])                                       
                else :                    
                    pcommet.children_comment.append(comment)                                       
                comment_list.append(pcommet)
            '''
    except Exception as e:
        print e
        logger.error(e)
    return render(request, 'blog/article.html', locals())

def add_article(request):
#    username = request.session.get('user')
    username = request.user.username
    user = User.objects.get(username=username)
    print user
    addarticle=AddArticleForm(request.POST)
    
    if addarticle.is_valid() :
        #死机在此处
        tag = Tag.objects.create(name = addarticle.cleaned_data["tag"],user=user)
        category= Category.objects.create(name = addarticle.cleaned_data["category"])
        #tag.save()
        article = Article.objects.create(user=user,                                                                         
                                title=addarticle.cleaned_data["title"],
                                desc=addarticle.cleaned_data["desc"],
                                content=addarticle.cleaned_data["content"],
                                category=category,
                                date_publish = datetime.datetime.now()
                                )         
        article.save()
        article.tag.add(tag)
    else :  
        return render(request, 'blog/failure.html', {'reason': addarticle.errors})                             
    
    #return render(request, 'blog/public_article.html', {'article': article, 'user': user, 'List': json.dumps(['文章发布成功', ])})
    return redirect(reverse(blog.views.index))

# 提交评论
def comment_post(request):
    try:
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            #获取表单信息
                                
            comment = Comment.objects.create(username=comment_form.cleaned_data["author"],
                                             email=comment_form.cleaned_data["email"],
                                             url=comment_form.cleaned_data["url"],
                                             content=comment_form.cleaned_data["comment"],
                                             article_id=comment_form.cleaned_data["article"],
                                             user=request.user if request.user.is_authenticated() else None
                                            #pid=comment_form.cleaned_data["pid"] if comment_form.cleaned_data["pid"]
                                             )                                                        
            comment.save()
        else:
            return render(request, 'blog/failure.html', {'reason': comment_form.errors})
    except Exception as e:
        logger.error(e)
    return redirect(request.META['HTTP_REFERER'])


def category(request):
    try:
        # 先获取客户端提交的信息
        cid = request.GET.get('cid', None)
        try:
            category = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return render(request, 'blog/failure.html', {'reason': '分类不存在'})
        article_list = Article.objects.filter(category=category)
        article_list = getPage(request, article_list)
    except Exception as e:
        logger.error(e)
    return render(request, 'blog/category.html', locals())

# 注销
def do_logout(request):
    try:
        logout(request)
    except Exception as e:
        print e
        logger.error(e)
    return redirect(request.META['HTTP_REFERER'])

# 注册
def do_reg(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                # 注册
                user = User.objects.create(username=reg_form.cleaned_data["username"],
                                    email=reg_form.cleaned_data["email"],
                                    url=reg_form.cleaned_data["url"],
                                    password=make_password(reg_form.cleaned_data["password"]),)
                user.save()

                # 登录
                user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
                login(request, user)
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'blog/failure.html', {'reason': reg_form.errors})
        else:
            reg_form = RegForm()
    except Exception as e:
        logger.error(e)
    return render(request, 'blog/reg.html', locals())

# 登录
def do_login(request):
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                # 登录
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式
                    login(request, user)
                else:
                    return render(request, 'blog/failure.html', {'reason': '登录验证失败'})
                return redirect(request.POST.get('source_url'))
            else:
                return render(request, 'blog/failure.html', {'reason': login_form.errors})
        else:
            login_form = LoginForm()
    except Exception as e:
        logger.error(e)
    return render(request, 'blog/login.html', locals())

@login_required
def changepwd(request):
    if request.method == 'GET':
        form = ChangepwdForm()
        return render(request, 'password/changepwd.html', locals())
    else:
        form = ChangepwdForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                user.set_password(newpassword)
                user.save()
                changepwd_success=True
                return render(request, 'password/index.html',locals())
            else:
                oldpassword_is_wrong=True
                return render(request,'password/changepwd.html', locals())
        else:
            return render(request,'password/changepwd.html',locals())
'''
通过发送邮件修改密码，使用官方提供的办法，修改成自定义的页面,本想增加中间层
'''        
def forgot_password(request):
    #可自定义表单，发送协议，
    return auth_views.password_reset(request,template_name='password/password_forgotpwd.html',
                                     email_template_name='password/password_reset_email.html',
                                     subject_template_name='password/password_reset_subject.txt')

def password_reset_done(request):
    #发送邮件完成跳转到这里
    return auth_views.password_reset_done(request, template_name='password/password_reset_done.html')

def password_reset_confirm(request,uidb64=None, token=None):
    #邮件修改密码页面
    return auth_views.password_reset_confirm(request, uidb64=uidb64, token=token, template_name='password/password_reset_confirm.html')

def password_reset_complete(request):
    #邮件密码修改完成显示
    return auth_views.password_reset_done(request, template_name='password/password_reset_complete.html')
