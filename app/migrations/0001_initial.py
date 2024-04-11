# Generated by Django 5.0.4 on 2024-04-11 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("BookID", models.IntegerField(primary_key=True, serialize=False)),
                ("BookName", models.CharField(max_length=200)),
                ("NumberOfCopies", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Member",
            fields=[
                ("MemberID", models.IntegerField(primary_key=True, serialize=False)),
                ("MemberName", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Circulation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField()),
                (
                    "eventtype",
                    models.CharField(
                        choices=[("checkout", "checkout"), ("return", "return")],
                        max_length=30,
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="circulations",
                        to="app.book",
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="circulations",
                        to="app.member",
                    ),
                ),
            ],
        ),
    ]