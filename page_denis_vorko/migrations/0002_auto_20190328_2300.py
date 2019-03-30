# Generated by Django 2.1.7 on 2019-03-28 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page_denis_vorko', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='author',
            field=models.ForeignKey(default='Denis Vorko', help_text='author', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='page_denis_vorko.Author'),
        ),
    ]