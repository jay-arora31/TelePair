# Generated by Django 3.0 on 2023-02-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_normaluser_shop_shopbrands_shopservice_tvbrands_tvservices'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='s_phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
