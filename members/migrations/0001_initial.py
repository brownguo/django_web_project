# Generated by Django 3.1.3 on 2020-11-13 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edit_time', models.DateTimeField(auto_created=True, verbose_name='CreatedTime')),
                ('created_time', models.DateTimeField(auto_created=True, verbose_name='CreatedTime')),
                ('username', models.CharField(default=None, max_length=200, verbose_name='会员名称')),
                ('mobile_no', models.CharField(default=None, max_length=100, verbose_name='手机号')),
                ('goods', models.CharField(default=None, max_length=200, verbose_name='商品名称')),
                ('address', models.TextField()),
                ('express_no', models.CharField(default=None, max_length=100, verbose_name='快递单号')),
                ('created_user', models.CharField(default=None, max_length=100, verbose_name='CraetedUser')),
                ('created_ip', models.CharField(max_length=100, verbose_name='CreatedIP')),
                ('project_id', models.CharField(max_length=100, verbose_name='ProID')),
            ],
            options={
                'verbose_name': '会员列表',
                'verbose_name_plural': '会员列表',
                'db_table': 'members_userinfo',
            },
        ),
    ]
