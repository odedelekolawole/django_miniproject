# Generated by Django 4.2.4 on 2023-08-07 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal1',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]