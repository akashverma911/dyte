# Generated by Django 3.2.10 on 2023-11-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElasticDemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.TextField()),
                ('message', models.TextField()),
                ('resourceId', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('traceId', models.TextField()),
                ('spanId', models.TextField()),
                ('commit', models.TextField()),
                ('metadata', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
