# Generated by Django 2.2.16 on 2023-02-16 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20230216_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=200, verbose_name='текст'),
        ),
    ]
