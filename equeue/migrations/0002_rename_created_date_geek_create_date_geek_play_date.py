# Generated by Django 5.1.2 on 2024-10-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equeue', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geek',
            old_name='created_date',
            new_name='create_date',
        ),
        migrations.AddField(
            model_name='geek',
            name='play_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
