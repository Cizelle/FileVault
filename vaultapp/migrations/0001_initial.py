# Generated by Django 5.2.2 on 2025-06-05 17:13

import uuid
import vaultapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileVault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('encrypted_file', models.FileField(upload_to=vaultapp.models.upload_to)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField()),
                ('is_viewed', models.BooleanField(default=False)),
            ],
        ),
    ]
