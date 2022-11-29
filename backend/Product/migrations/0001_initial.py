# Generated by Django 4.1.3 on 2022-11-23 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0003_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('details', models.TextField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.color')),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.material')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.size')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]