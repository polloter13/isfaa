# Generated by Django 4.0.5 on 2023-02-20 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_gübre_alter_tool_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='gübre',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/fertilizers/', verbose_name='Şəkil'),
        ),
        migrations.AlterField(
            model_name='texnika',
            name='image',
            field=models.ImageField(upload_to='images/techniques/', verbose_name='Şəkil'),
        ),
    ]
