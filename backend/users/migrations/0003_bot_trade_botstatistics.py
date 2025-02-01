# Generated by Django 4.2.18 on 2025-02-01 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_groups_user_is_active_user_is_staff_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bot",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("premium", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Trade",
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
                ("trade_time", models.DateTimeField()),
                (
                    "trade_type",
                    models.CharField(
                        choices=[("BUY", "Buy"), ("SELL", "Sell")], max_length=10
                    ),
                ),
                ("asset", models.CharField(max_length=50)),
                ("amount", models.DecimalField(decimal_places=8, max_digits=20)),
                ("price", models.DecimalField(decimal_places=2, max_digits=20)),
                ("profit_loss", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "status",
                    models.CharField(
                        choices=[("OPEN", "Open"), ("CLOSED", "Closed")], max_length=10
                    ),
                ),
                (
                    "bot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.bot"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BotStatistics",
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
                ("total_trades", models.IntegerField()),
                ("win_rate", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "avg_trading_rate",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "total_trade_volume",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                ("number_of_users", models.IntegerField()),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "bot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.bot"
                    ),
                ),
            ],
        ),
    ]
