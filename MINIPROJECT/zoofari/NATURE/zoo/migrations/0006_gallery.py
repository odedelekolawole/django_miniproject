# Generated by Django 4.2.4 on 2023-08-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0005_specialservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='gallery')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
    ]
