# Generated by Django 2.1 on 2018-09-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miaTest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiatestPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'miatest_person',
                'managed': False,
            },
        ),
    ]
