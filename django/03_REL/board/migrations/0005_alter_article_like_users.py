# Generated by Django 4.2.5 on 2023-10-16 14:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0004_alter_article_user_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='like_users',
            field=models.ManyToManyField(default=0, related_name='like_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
