# Generated by Django 3.0.7 on 2021-04-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'tableuser',
            },
        ),
    ]
