from django.db import models
class Account(models.Model):
    name = models.CharField(max_length=20)
    wechat_id = models.CharField(max_length=10)
    introduction = models.CharField(max_length=200)
    last_updated = models.DateField()
class Article(models.Model):
    title = models.CharField(max_length=125)
    description = models.CharField(max_length=340, null=True)
    text_url = models.URLField(max_length=255)
    text = models.TextField(null=True)
    publication_date = models.DateField()
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE)
