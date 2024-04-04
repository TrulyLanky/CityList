# Generated by Django 4.2.10 on 2024-04-04 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Name', max_length=200)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
