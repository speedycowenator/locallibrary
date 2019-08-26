# Generated by Django 2.2.4 on 2019-08-21 00:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_testarticle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleinstance',
            name='Article',
        ),
        migrations.DeleteModel(
            name='TestArticle',
        ),
        migrations.AlterField(
            model_name='article',
            name='Publication',
            field=models.CharField(default=1.0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='article',
            name='topic',
        ),
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.CharField(default='No Topic', max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ArticleInstance',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]