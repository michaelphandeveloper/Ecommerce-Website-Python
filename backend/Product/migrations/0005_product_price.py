# Generated by Django 4.1.3 on 2022-11-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_rename_materials_product_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=25, null=True),
        ),
    ]