from django.db import models

# Create your models here.


# 存储抓取过来的信息
class CrawlData(models.Model):
    content = models.CharField(null=True,max_length=50000)
   # crawl_time = models.DateTimeField(null=True)
    emotion = models.IntegerField(null=True)
    is_agriculture = models.IntegerField(null=True)
    keywords = models.CharField(null=True,max_length=50)
    publish_time = models.CharField(null=True,max_length=50)
    source = models.CharField(null=True,max_length=50)
    summary = models.CharField(null=True,max_length=5000)
    title = models.CharField(null=True,max_length=500)
    url = models.CharField(null=True,max_length=255)
    industry = models.CharField(null=True,max_length=500)
    area = models.CharField(null=True,max_length=50)
    product_name = models.CharField(null=True, max_length=500)
    status =  models.IntegerField(null=True)



# 存储了需要抓取的模块信息
class CrawModel(models.Model):

    crawl_start_url = models.CharField(null=True,max_length=255)
    web_name = models.CharField(null=True,max_length=255)
    level_1 = models.CharField(null=True, max_length=255)
    level_2 = models.CharField(null=True, max_length=255)
    level_3 = models.CharField(null=True, max_length=255)
    crawl_max_page = models.IntegerField(null=True)


class ProductNameToCate(models.Model):

    keyname =  models.CharField(null=True,max_length=255)
    product_name = models.CharField(null=True,max_length=255)

class Area(models.Model):
    code = models.CharField(max_length=6, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)


class EmotionKeyword(models.Model):
    start = models.CharField(max_length=255, blank=True, null=True)
    end = models.CharField(max_length=255, blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    min_times = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    is_use = models.CharField(max_length=255, blank=True, null=True)










    
    


