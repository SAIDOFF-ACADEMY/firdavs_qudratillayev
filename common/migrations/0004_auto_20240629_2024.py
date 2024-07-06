# Generated by Django 4.2.3 on 2024-06-29 15:24

from django.db import migrations
from common.models import Settings


def settings_create(*args, **kwargs):
    Settings.objects.create(
        contact_telegram='chereuz',
        longitude=0,
        latitude=0,
        locations_text='text',
        working_horse_start='00:00:00',
        working_horse_end='23:59:59',
        telegram_bot='chereuzbot'
    )


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0003_alter_settings_contact_phone'),
    ]
    atomic = False
    operations = [
        migrations.RunPython(settings_create),
    ]
