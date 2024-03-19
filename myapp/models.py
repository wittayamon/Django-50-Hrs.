from django.db import models

# Create your models here.
class Tracking(models.Model):
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    tracking = models.CharField(max_length=50,null=True,blank=True)
    other = models.TextField(null=True,blank=True)

    def __str__(self):
        return '{} - {} ({})'.format(self.name, self.tel, self.tracking)

class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    trendingnow=models.BooleanField(default=False)
    image=models.ImageField(upload_to="products",blank=True)

class askQA(models.Model):
    name=models.CharField(max_length=100,verbose_name='ชื่อผู้ติดต่อ')
    email=models.CharField(max_length=100,null=True,blank=True,verbose_name='อีเมล')
    title=models.CharField(max_length=100,null=True,blank=True,verbose_name='หัวห้อ')
    detail=models.TextField(max_length=100,null=True,blank=True,verbose_name='รายละเอียด')
    detail_asnwer=models.TextField(null=True,blank=True,verbose_name='คำตอบ')
    def __str__(self):
        return '{} : ({})'.format(self.name, self.title)
