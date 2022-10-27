# Generated by Django 4.1 on 2022-10-27 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=65535)),
                ('stock_qty', models.IntegerField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
