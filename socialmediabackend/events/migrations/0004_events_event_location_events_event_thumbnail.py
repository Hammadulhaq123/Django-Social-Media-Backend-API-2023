# Generated by Django 4.2.6 on 2023-10-22 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_events_event_organizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_location',
            field=models.CharField(default='Virtual Event', max_length=1000),
        ),
        migrations.AddField(
            model_name='events',
            name='event_thumbnail',
            field=models.ImageField(blank=True, upload_to='event_images'),
        ),
    ]