# Generated by Django 3.1.1 on 2021-06-13 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_comments_create_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='userapply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('second_name', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=64)),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
                ('position', models.CharField(blank=True, choices=[('Teacher', 'Teacher'), ('Front Desk', 'Front Desk'), ('Cashier', 'Cashier'), ('Care Unit', 'Care Unit'), ('Security ', 'Security'), ('Nanny ', 'Nanny')], default='Teacher', max_length=100, null=True)),
                ('department', models.CharField(blank=True, choices=[('Early Years', 'Early Years'), ('Primary', 'Primary'), ('Secondary ', 'Secondary'), ('ICT', 'ICT'), ('Music', 'Music'), ('Others ', 'Others')], default='Early Years', max_length=100, null=True)),
                ('about', models.TextField()),
                ('create_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/user_images')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='post/user_cv')),
            ],
            options={
                'verbose_name_plural': 'userapply',
            },
        ),
        migrations.RemoveField(
            model_name='users',
            name='department',
        ),
        migrations.RemoveField(
            model_name='users',
            name='pdf',
        ),
        migrations.RemoveField(
            model_name='users',
            name='position',
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
