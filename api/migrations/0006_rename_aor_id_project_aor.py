# Generated by Django 3.2.4 on 2021-08-20 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210820_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='aor_id',
            new_name='aor',
        ),
    ]