# Generated by Django 2.0.7 on 2018-07-21 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=160)),
                ('choice', models.CharField(max_length=200)),
            ],
        ),
    ]
