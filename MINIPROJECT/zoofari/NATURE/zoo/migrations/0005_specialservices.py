# Generated by Django 4.2.4 on 2023-08-07 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0004_animal1_login_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icons', models.ImageField(upload_to='icons')),
                ('services', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'SpecialServices',
            },
        ),
    ]