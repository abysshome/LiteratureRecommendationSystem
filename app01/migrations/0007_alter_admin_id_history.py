# Generated by Django 4.2.9 on 2024-02-26 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app01", "0006_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admin",
            name="id",
            field=models.AutoField(
                primary_key=True, serialize=False, verbose_name="身份证"
            ),
        ),
        migrations.CreateModel(
            name="History",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="id"
                    ),
                ),
                ("text", models.CharField(max_length=32, verbose_name="搜索内容")),
                ("time", models.DateTimeField(auto_now_add=True, verbose_name="搜索时间")),
                (
                    "user",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app01.admin",
                        verbose_name="所属用户",
                    ),
                ),
            ],
        ),
    ]
