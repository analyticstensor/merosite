# Generated by Django 4.2.8 on 2024-01-27 20:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('email', models.EmailField(max_length=50, verbose_name='email')),
                ('subject', models.CharField(max_length=150, verbose_name='subject')),
                ('message', models.TextField(max_length=5000, verbose_name='message')),
                ('message_received_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='message received datetime')),
                ('user_id', models.BigIntegerField(blank=True, default=None, null=True, verbose_name='user Id')),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
