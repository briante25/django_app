# Generated by Django 4.2 on 2024-01-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_report_alter_mysite_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysite',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='mysite',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mysite',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
