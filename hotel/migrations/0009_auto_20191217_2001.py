# Generated by Django 2.2.7 on 2019-12-17 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_auto_20191217_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='RoomNumber',
            new_name='roomnumber',
        ),
    ]