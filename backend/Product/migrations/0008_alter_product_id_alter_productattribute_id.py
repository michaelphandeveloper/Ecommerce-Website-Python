# Generated by Django 4.1.3 on 2022-11-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_auto_20221125_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]