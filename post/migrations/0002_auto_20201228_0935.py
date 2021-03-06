# Generated by Django 3.1.1 on 2020-12-28 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('second_name', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=64)),
                ('comments', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'posts'},
        ),
    ]
