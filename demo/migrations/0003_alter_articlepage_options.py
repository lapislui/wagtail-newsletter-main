# Generated by Django 5.0.6 on 2024-06-20 15:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("demo", "0002_articlepage_newsletter_mixin"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="articlepage",
            options={
                "permissions": [("sendnewsletter_articlepage", "Can send newsletter")]
            },
        ),
    ]
