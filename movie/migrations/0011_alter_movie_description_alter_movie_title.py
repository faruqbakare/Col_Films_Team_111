# Generated by Django 4.1 on 2022-08-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_movie_upload_date_alter_movie_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
