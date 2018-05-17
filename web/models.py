from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '用户名：' + self.username + '    密码：' + self.password + '    姓名： ' + self.name

class Access_log(models.Model):
    path = models.TextField(max_length=100)
    get_param = models.CharField(max_length=100)
    post_param = models.CharField(max_length=100)
    access_time = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    user_agent = models.CharField(max_length=100)

    def __str__(self):
        return 'id:' + str(self.id) + '&path:' + str(self.path) + \
               '&get:' + self.get_param + '&post:' + self.post_param + \
               '&access_time:' + str(self.access_time) + '&ip_address:' + self.ip_address + \
               '&ip_address:' + self.ip_address + '&location:' + self.location + \
               '&user_agent:' + self.user_agent

class News(models.Model):
    title = models.TextField(max_length=1000)
    content = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'title:' + self.title + "   " + "content：" + self.content

class LiuYan(models.Model):
    username = models.TextField(max_length=100)
    content = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)