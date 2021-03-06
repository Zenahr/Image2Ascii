# Generated by Django 3.1.2 on 2020-12-05 16:23

import django_migration_linter
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_generatedascii_imagetoasciitype_outputascii_report_texttoasciitype'),
    ]

    operations = [
        django_migration_linter.IgnoreMigration(),
        migrations.AlterField(
            model_name='generatedascii',
            name='url_code',
            field=models.CharField(editable=False, max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='outputascii',
            name='ascii_txt',
            field=models.TextField(default=''),
        ),
    ]
