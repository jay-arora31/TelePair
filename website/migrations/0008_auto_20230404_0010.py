# Generated by Django 3.1.10 on 2023-04-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_requestapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
