# Generated by Django 4.0.5 on 2022-12-28 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='mehsul_zamani',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
