from django.db import models

# Create your models here.

from django.contrib.auth.models import User,AbstractUser

class UserInfo(AbstractUser):
	# 继承auto_user这张表
	nid = models.AutoField(primary_key=True)
	def __str__(self):
		return self.username

class Classify(models.Model):
	# 分类表
	nid = models.AutoField(primary_key=True)
	classify_name = models.CharField(verbose_name="分类标题",max_length=11,null=True,unique=True)
	user = models.ForeignKey(to="UserInfo",to_field="nid", on_delete=models.CASCADE)

class Article(models.Model):
	#文章表
	nid = models.AutoField(primary_key=True)
	title = models.CharField(verbose_name="文章标题",max_length=11,null=True)
	time = models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
	content = models.TextField(verbose_name="文章内容",null=True)
	classify = models.ForeignKey(verbose_name="所属分类",to="Classify",to_field="nid",on_delete=models.CASCADE)

class Comment(models.Model):
	#评论表
	nid = models.AutoField(primary_key=True)
	comment_name = models.CharField(verbose_name="评论名",max_length=11,null=True)
	comment_content = models.TextField(null=True)
	article = models.ForeignKey(verbose_name="所属文章",to="Article",to_field="nid",on_delete=models.CASCADE)
