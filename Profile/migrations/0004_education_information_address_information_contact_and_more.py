# Generated by Django 4.1.7 on 2023-03-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_alter_information_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.DateField()),
                ('Level', models.CharField(max_length=250)),
                ('School', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='information',
            name='Address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='Contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
