# Generated by Django 3.1.4 on 2020-12-02 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_delete_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='offer',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='category',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='user',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.DeleteModel(
            name='Offers',
        ),
    ]