from django.shortcuts import render,HttpResponse,redirect
from django.db.models import Avg,Count,Min,Max
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Gavin import models
from django.contrib import auth
import re,time,os,json
from Gavin_blog import settings
# Create your views here.


def home(request):
	# 主页
	name = 'Gavin'
	article = []
	for a in models.Article.objects.all():
		commnet_count = len(a.comment_set.all())
		# 过滤文章中的html标签
		content = a.content[:2000]
		content = re.sub('<.*?>',"",content)
		content = re.sub("\s*","",content)
		# 改变时间的格式
		time_1 = a.time.strftime('%Y-%m-%d')
		print(time_1,type(time_1))
		article.append([a.title,content[:400],time_1,commnet_count,a.nid])
	return render(request,"home.html",{"name":name,"article":article})

def article(request,nid):
	# 文章详情页
	article_1 = models.Article.objects.filter(nid=nid).first()
	article_2 = {"title":article_1.title,"content":article_1.content,"time":article_1.time.strftime('%Y-%m-%d'),"nid":article_1.nid}
	# 取分类表的数据
	classify = models.Classify.objects.all()
	classfiy_list = []
	for a in classify:
		classify_count = len(a.article_set.all())
		classfiy_list.append([a.classify_name,classify_count])
	article_2["classify"] = classfiy_list
	# 取评论表的数据
	comment = article_1.comment_set.all()
	# 判断是否有评论，有则放入列表中，最后赋值给article_2字典
	if comment:
		comment_list = []
		for a in comment:
			comment_list.append([a.comment_name, a.comment_content])
		article_2["comment"] = comment_list
	else:
		article_2["comment"] = None
	return render(request,"article.html",{"article_2":article_2})

def login(request):
	# 登录
	if request.method == "POST":
		user = request.POST.get("username").strip()
		password = request.POST.get("password").strip()
		print(user,password)
		user = auth.authenticate(username = user,password=password)
		if user:
			print("成功")
			auth.login(request,user)
			return redirect("/create_article/")
	return render(request,"login.html")

@login_required
def logout(request):
	# 注销
	print(request.user.is_anonymous)
	auth.logout(request)
	print("注销成功")
	print(request.user)
	return redirect("/home/")

@login_required
def create_article(request):
	# 用户的增删改查
	article_list = []
	for a in models.Article.objects.all():
		article_dict = {}
		article_dict["nid"] = a.nid
		article_dict["title"] = a.title
		article_dict["time"] = a.time
		article_list.append(article_dict)
	return render(request,"create_article.html",{"article_list":article_list})

@login_required
def new_article(request):
	# 添加新随笔
	if request.method == "POST":
		data = {}
		title = request.POST.get("title")
		article = request.POST.get("article")
		classify_id = int(request.POST.get("classify"))
		models.Article.objects.create(title=title,content=article,classify_id=classify_id)
		data["succeed"] = True
		return JsonResponse(data)
	# 返回页面
	classify_list = []
	for i in models.Classify.objects.all():
		classify_dict = {}
		classify_dict["nid"] = i.nid
		classify_dict["classify_name"] = i.classify_name
		classify_list.append(classify_dict)
	return render(request,"new_article.html",{"classify_list":classify_list})

@login_required
def delete(request):
	# 删除指定的文章
	nid = int(request.POST.get("nid"))
	models.Article.objects.filter(nid=nid).first().delete()
	data = {}
	data["succeed"] = True
	return JsonResponse(data)

def classify_article(request,classify):
	# 查看文章分类
	# 去分类表的文章
	article_1 = models.Classify.objects.filter(classify_name=classify).first().article_set.all()
	article_list = []
	for a in article_1:
		article_a_list = []
		comment_count = len(a.comment_set.all())
		article_a_list.append(a.title)
		content = a.content[:2000]
		content = re.sub('<.*?>', "", content)
		content = re.sub("\s*", "", content)
		article_a_list.append(content[:350])
		article_a_list.append(a.time)
		article_a_list.append(comment_count)
		article_a_list.append(a.nid)
		article_list.append(article_a_list)
	article_2 = {"article_list":article_list}
	# 取分类表的数据
	classify = models.Classify.objects.all()
	classfiy_list = []
	for a in classify:
		classify_count = len(a.article_set.all())
		classfiy_list.append([a.classify_name,classify_count])
	article_2["classify_list"] = classfiy_list
	return render(request,"classify_article.html",{"article_2":article_2})

def create_comment(request):
	# 提交评论处理
	comment_name = request.POST.get("comment_name")
	comment_content = request.POST.get("comment_content")
	article_nid = request.POST.get("article_nid")
	models.Comment.objects.create(comment_name=comment_name,comment_content=comment_content,article_id = article_nid)
	dictvar = {"succeed":True}
	return JsonResponse(dictvar)

def contact(request):
	# 联系方式
	return render(request,"contact.html")

def upload(request):
	# 添加文章时上传的图片
	img = request.FILES.get("upload_img")
	img_name = img.name
	path = os.path.join(os.path.join(settings.BASE_DIR,"static"),"img",img_name)
	print(path)
	with open(path,"wb") as fp:
		for a in img:
			fp.write(a)
	response = {
		"error":0,
		"url":"/static/img/%s"%(img_name)
	}
	return HttpResponse(json.dumps(response))

@login_required
def new_classify(request):
	print(request.user)
	# 添加新分类
	if request.method == "POST":
		classify = request.POST.get("classify")
		models.Classify.objects.create(classify_name=classify,user = request.user)
		data = {}
		data["succeed"] = True
		return JsonResponse(data)
	return render(request,"new_classify.html")

