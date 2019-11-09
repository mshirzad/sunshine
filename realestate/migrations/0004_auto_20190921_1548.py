# Generated by Django 2.2.4 on 2019-09-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0003_auto_20190919_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='phone_no',
            new_name='phone_no1',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='email',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='last_name',
        ),
        migrations.AddField(
            model_name='address',
            name='phone_no2',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
