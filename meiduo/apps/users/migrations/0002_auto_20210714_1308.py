# Generated by Django 2.1.7 on 2021-07-14 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(help_text='手机号', max_length=11, unique=True, verbose_name='手机号'),
        ),
    ]
