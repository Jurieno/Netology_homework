# Generated by Django 4.2.3 on 2023-07-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_article_scopes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(through='articles.Scope', to='articles.tag'),
        ),
    ]
