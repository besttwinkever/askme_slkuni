# Generated by Django 5.1.1 on 2024-11-10 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askme_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuaetionLike',
            new_name='QuestionLike',
        ),
    ]