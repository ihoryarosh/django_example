# Generated by Django 2.1.7 on 2019-03-30 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_denis_vorko', '0010_auto_20190329_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='jobs'),
        ),
    ]
