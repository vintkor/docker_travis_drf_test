# Generated by Django 2.2.2 on 2019-06-26 12:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('created', models.DateTimeField(auto_created=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
