# Generated by Django 5.0.3 on 2024-03-31 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uniquetodo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
