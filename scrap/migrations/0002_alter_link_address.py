# Generated by Django 5.1.1 on 2024-09-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='address',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
