# Generated by Django 4.1.3 on 2022-11-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0005_alter_brand_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=50)),
                ('alt_text', models.CharField(max_length=75)),
            ],
        ),
    ]