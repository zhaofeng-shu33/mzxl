# Generated by Django 2.1.5 on 2019-02-12 11:46

from django.db import migrations
import os
from wechatpy import WeChatClient
import yaml
import datetime
import pdb
def add_mzxl_center_account(apps, schema_editor):
    Account = apps.get_model('django_mzxl', 'Account')
    if(Account.objects.filter(wechat_id='mzxlhn')):
        return
    a = Account()
    a.name = '海南美在心灵'
    a.wechat_id = 'mzxlhn'
    a.introduction = '海南省“美在心灵”大学生支教志愿者协会，简称“美在心灵”，是以琼籍大学生为主的国内知名大学生NGO。美在心灵以“团结友爱，奉献社会”为宗旨，旨在筹集社会善款支持大学生为主的志愿者以知识文化反哺海南家乡，协助发展海南中小学等基础教育事业'
    a.last_updated = datetime.date(2013, 12, 1) # not valid
    a.save()
def get_wechat_client():
    with open(os.path.join(os.path.expanduser('~'), '.wechat.yaml')) as f:
        dic = yaml.load(f.read())
    client = WeChatClient(dic['app_id'], dic['app_secret'])
    return client
def update_news(news, update_time, account, Article):
    text_url = news['url']
    if(Article.objects.filter(text_url=text_url)):
        return
    a = Article()
    a.title = news['title']
    a.description = news['digest']
    a.text_url = text_url
    a.text = news['content']
    a.publication_date = datetime.datetime.fromtimestamp(update_time)
    a.account = account
    try:
        a.save()
    except Exception as e:
        pdb.set_trace()
    
def add_mzxl_center_article(apps, schema_editor):
    client = get_wechat_client().material
    j = client.get_count()
    Account = apps.get_model('django_mzxl', 'Account')
    Article = apps.get_model('django_mzxl', 'Article') 
    a = Account.objects.get(wechat_id='mzxlhn')
    news_count = j['news_count']
    print('total news: %d' % news_count) 
    offset = 0
    while(offset < news_count):
        j = client.batchget('news',offset=offset)
        for item in j['item']:
            for news in item['content']['news_item']:
                update_news(news, item['update_time'] ,a, Article)
        offset += 20
        print('current offset: %d' %offset)

class Migration(migrations.Migration):

    dependencies = [
        ('django_mzxl', '0003_auto_20190212_1218'),
    ]

    operations = [
        migrations.RunPython(add_mzxl_center_account),
        migrations.RunPython(add_mzxl_center_article)
    ]