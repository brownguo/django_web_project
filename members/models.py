from django.db import models

# Create your models here.


class Members(models.Model):
    username = models.CharField('会员名称', max_length=200, default=None)
    mobile_no = models.CharField('手机号', max_length=100, default=None)
    goods = models.CharField('商品名称', max_length=200, default=None)
    address = models.TextField()
    express_no = models.CharField('快递单号', max_length=100, default=None)
    created_user = models.CharField('CraetedUser', max_length=100, default=None)
    created_time = models.DateTimeField('CreatedTime', auto_created=True)
    edit_time = models.DateTimeField('CreatedTime', auto_created=True)
    created_ip = models.CharField('CreatedIP', max_length=100)
    project_id = models.CharField('ProID', max_length=100)

    class Meta:
        db_table = 'members_userinfo'
        verbose_name = '会员列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username