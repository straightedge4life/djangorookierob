# Generated by Django 2.2 on 2019-04-23 03:57

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', blog.models.UnsignedIntegerField(db_index=True, verbose_name='用户id')),
                ('content', models.TextField(default='', verbose_name='评论内容')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50, unique=True, verbose_name='用户名')),
                ('nickname', models.CharField(default='', max_length=100, verbose_name='用户昵称')),
                ('sex', blog.models.TinyIntegerField(db_index=True, default=0, verbose_name='性别')),
                ('phone', models.CharField(default='', max_length=20, verbose_name='手机号')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='电子邮箱')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
        ),
    ]