# Generated by Django 4.2.5 on 2023-10-06 02:22

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articletwo',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('article_title', models.CharField(max_length=200)),
                ('article_published', models.DateTimeField(verbose_name='date published')),
                ('article_content', tinymce.models.HTMLField()),
                ('article_url', models.CharField(max_length=100)),
                ('article_image', models.ImageField(upload_to='post/')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
