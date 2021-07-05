# Generated by Django 3.2.5 on 2021-07-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.BooleanField(default=True)),
                ('slug', models.CharField(blank=True, max_length=200, null=True, unique=True)),
            ],
        ),
    ]