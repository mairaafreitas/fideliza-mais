# Generated by Django 4.0 on 2021-12-20 11:22

from django.db import migrations, models

import user.validators


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="document",
            field=models.CharField(
                max_length=11, unique=True, validators=[user.validators.cpf_validator]
            ),
        ),
    ]
