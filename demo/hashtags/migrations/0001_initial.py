# Generated by Django 2.1.1 on 2018-10-31 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
