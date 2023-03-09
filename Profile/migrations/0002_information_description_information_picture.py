# Generated by Django 4.1.7 on 2023-03-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='Description',
            field=models.TextField(default='', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='information',
            name='Picture',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]