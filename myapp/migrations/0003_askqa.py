# Generated by Django 4.2 on 2024-03-02 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='askQA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='ชื่อผู้ติดต่อ')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='อีเมล')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='หัวห้อ')),
                ('detail', models.TextField(blank=True, max_length=100, null=True, verbose_name='รายละเอียด')),
            ],
        ),
    ]