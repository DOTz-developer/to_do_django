# Generated by Django 4.1.7 on 2023-03-30 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mod",
            name="date",
            field=models.DateField(default="4888-03-25"),
            preserve_default=False,
        ),
    ]