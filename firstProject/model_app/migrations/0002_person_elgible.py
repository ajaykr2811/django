# Generated by Django 5.0.6 on 2024-07-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("model_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="elgible",
            field=models.BooleanField(default=False),
        ),
    ]