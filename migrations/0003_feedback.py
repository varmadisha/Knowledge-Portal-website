# Generated by Django 5.0.2 on 2024-03-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lkp', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_message', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'feed',
                'ordering': ['-email'],
            },
        ),
    ]
