# Generated by Django 2.2.27 on 2023-02-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20230214_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='s_image',
            field=models.ImageField(blank=True, null=True, upload_to='Shop/'),
        ),
    ]
