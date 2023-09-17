# Generated by Django 4.2.5 on 2023-09-17 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('catagory', models.CharField(max_length=30)),
                ('uses', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
