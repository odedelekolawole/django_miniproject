# Generated by Django 4.2.4 on 2023-08-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lion', models.ImageField(upload_to='animal1')),
            ],
            options={
                'verbose_name_plural': 'Animal1',
            },
        ),
    ]
