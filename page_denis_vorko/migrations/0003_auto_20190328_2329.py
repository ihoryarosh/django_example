# Generated by Django 2.1.7 on 2019-03-28 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_denis_vorko', '0002_auto_20190328_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='author',
            field=models.CharField(default='Denis Vorko', max_length=56),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
