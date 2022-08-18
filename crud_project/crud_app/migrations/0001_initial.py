# Generated by Django 4.1 on 2022-08-18 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crud_models',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, max_length=30)),
                ('product_price', models.IntegerField()),
                ('product_created_date', models.DateField()),
            ],
            options={
                'db_table': 'crud_table',
            },
        ),
    ]
