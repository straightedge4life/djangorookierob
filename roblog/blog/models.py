from django.db import models
from django.utils import timezone

class UnsignedIntegerField(models.IntegerField):
    
    def db_type(self, connection):
        if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
            return 'integer UNSIGNED'

class TinyIntegerField(models.SmallIntegerField):
    def db_type(self, connection):
        if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
            return "tinyint"
       


class users(models.Model):
    username = models.CharField('用户名' , max_length = 50 , unique = True , default = '' )
    nickname = models.CharField('用户昵称' , max_length=100 ,  default = '')
    sex      = TinyIntegerField('性别 0保密 1男 2女' ,  default = 0 , db_index = True)
    phone    = models.CharField('手机号' ,  max_length=20 ,  default = '')
    email    = models.EmailField('电子邮箱' , max_length=254 ,  default = '')
    add_time = models.DateTimeField('添加时间' ,   auto_now_add=True)
    is_active = TinyIntegerField('是否激活' , default = 0 )
    
    

        
class comments(models.Model) :
    user_id = UnsignedIntegerField('用户id' , db_index = True)
    content = models.TextField('评论内容' ,  default = '')
    add_time = models.DateField('添加时间', auto_now_add=True)

