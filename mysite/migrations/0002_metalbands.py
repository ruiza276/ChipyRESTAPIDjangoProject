# Generated by Django 2.2.7 on 2019-11-27 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetalBands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.TextField()),
                ('fans', models.IntegerField()),
                ('formed', models.IntegerField()),
                ('origin', models.TextField()),
                ('split', models.TextField()),
                ('style', models.TextField()),
            ],
        ),
    ]
