# Generated by Django 2.0.1 on 2018-07-20 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20180720_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='manager_person',
            field=models.ForeignKey(default=None, null=True, on_delete='SET_DEFAULT', to='assets.Manager_persion'),
        ),
    ]
