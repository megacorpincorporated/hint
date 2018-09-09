# Generated by Django 2.1 on 2018-09-06 16:54

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.IntegerField(editable=False)),
                ('is_dummy', models.BooleanField(default=False)),
                ('heartbeat', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceConfiguration',
            fields=[
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='device.Device')),
                ('configuration', django.contrib.postgres.fields.jsonb.JSONField()),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
