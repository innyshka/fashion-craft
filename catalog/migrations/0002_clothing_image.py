# Generated by Django 4.2.5 on 2023-09-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/clothing'),
        ),
    ]
