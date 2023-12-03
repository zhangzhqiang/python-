from django.db import models


# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)  # 自增,主键
    title = models.CharField(max_length=32, unique=True)  # varchar类型,唯一约束
    pub_date = models.DateField()  # 存日期
    price = models.DecimalField(max_digits=8, decimal_places=2)  # 浮点型,最大八位保留两位小数
    publish = models.CharField(max_length=32)  # varchar类型

    def __str__(self):
        return self.title



