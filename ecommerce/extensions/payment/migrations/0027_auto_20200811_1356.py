# Generated by Django 2.2.15 on 2020-08-11 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0026_auto_20200305_1448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enterprisecontractmetadata',
            options={'get_latest_by': 'modified'},
        ),
    ]