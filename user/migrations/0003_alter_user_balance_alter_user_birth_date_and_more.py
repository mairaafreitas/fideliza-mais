# Generated by Django 4.0 on 2021-12-21 11:57

import django.core.validators
from django.db import migrations, models

import user.validators


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_user_document"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="balance",
            field=models.IntegerField(default=0, verbose_name="Pontuação"),
        ),
        migrations.AlterField(
            model_name="user",
            name="birth_date",
            field=models.DateField(verbose_name="Data de Nascimento"),
        ),
        migrations.AlterField(
            model_name="user",
            name="document",
            field=models.CharField(
                max_length=11,
                unique=True,
                validators=[user.validators.cpf_validator],
                verbose_name="CPF",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=80, verbose_name="Nome"),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(
                max_length=11,
                unique=True,
                validators=[django.core.validators.MinLengthValidator(11)],
                verbose_name="Celular",
            ),
        ),
    ]
