# Generated by Django 4.0.5 on 2022-06-29 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_body_post_created_at_post_name'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='posts',
        ),
    ]