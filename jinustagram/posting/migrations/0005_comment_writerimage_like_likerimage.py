# Generated by Django 4.0.6 on 2022-10-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0004_storyviewer_viewerimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='writerImage',
            field=models.ImageField(default='\\default.png', upload_to='%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='like',
            name='likerImage',
            field=models.ImageField(default='\\default.png', upload_to='%Y/%m/%d'),
        ),
    ]
