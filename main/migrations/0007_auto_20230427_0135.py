# Generated by Django 2.2.5 on 2023-04-26 20:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20230426_2317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='role',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='service',
            name='charges',
        ),
        migrations.AddField(
            model_name='service',
            name='shop_brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.ShopBrands'),
        ),
        migrations.AddField(
            model_name='service',
            name='shop_service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.ShopService'),
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Category'),
        ),
        migrations.AlterField(
            model_name='service',
            name='company',
            field=models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Company'),
        ),
        migrations.AlterField(
            model_name='service',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 27, 1, 35, 29, 103341), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='service',
            name='location',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Location'),
        ),
    ]
