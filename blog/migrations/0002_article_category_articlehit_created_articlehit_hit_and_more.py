# Generated by Django 4.1.2 on 2022-12-20 02:43

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_member_event"),
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="articles",
                to="courses.category",
            ),
        ),
        migrations.AddField(
            model_name="articlehit",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="articlehit",
            name="hit",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="courses.hitdetail",
            ),
        ),
        migrations.AddField(
            model_name="articletag",
            name="tag",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="courses.tag",
            ),
        ),
    ]
