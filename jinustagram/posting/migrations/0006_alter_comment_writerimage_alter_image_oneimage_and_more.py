# Generated by Django 4.0.6 on 2022-10-19 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0005_comment_writerimage_like_likerimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='writerImage',
            field=models.ImageField(default='default.png', upload_to='%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='image',
            name='Oneimage',
            field=models.ImageField(default='default.png', upload_to='%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='like',
            name='likerImage',
            field=models.ImageField(default='default.png', upload_to='%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='story',
            name='storyImage',
            field=models.ImageField(default='default.png', upload_to='%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='storyviewer',
            name='storyId',
            field=models.ForeignKey(db_column='story_id', on_delete=django.db.models.deletion.CASCADE, related_name='storyViewerPost', to='posting.story'),
        ),
        migrations.AlterField(
            model_name='storyviewer',
            name='viewerImage',
            field=models.ImageField(default='default.png', upload_to='%Y/%m/%d'),
        ),
    ]
