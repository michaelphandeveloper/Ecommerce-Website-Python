# Generated by Django 4.1.3 on 2022-11-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=25, null=True),
        ),
    ]