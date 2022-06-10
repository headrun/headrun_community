# Generated by Django 4.0.5 on 2022-06-10 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventphotos',
            name='event_file',
            field=models.FileField(default=1, upload_to='static/', verbose_name='event_images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventphotos',
            name='event_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='event_user', to='community.events'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='events',
            name='event_descript',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='event_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_feedbackid', to='community.events'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='given_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='given_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]