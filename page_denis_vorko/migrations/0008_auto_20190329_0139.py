# Generated by Django 2.1.7 on 2019-03-28 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_denis_vorko', '0007_auto_20190329_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='page_denis_vorko/static/page_denis_vorko/img/'),
        ),
    ]