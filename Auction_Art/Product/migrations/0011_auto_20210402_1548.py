# Generated by Django 3.0.7 on 2021-04-02 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0010_auto_20210402_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bidEndDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='bidStartDate',
            field=models.DateField(null=True),
        ),
    ]
