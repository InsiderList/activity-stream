# Generated by Django 3.2.15 on 2022-09-25 22:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('insiderlist', '0002_initial'),
        ('actstream', '0004_action_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='issuer',
            field=models.ForeignKey(default=0, help_text='Issuer subject to MAR for delayed disclosure', on_delete=django.db.models.deletion.CASCADE, to='insiderlist.issuer', verbose_name='Issuer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='action',
            name='obj_created_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='action',
            name='obj_updated_datetime',
            field=models.DateTimeField(auto_now=True, verbose_name='Last updated'),
        ),
        migrations.AlterField(
            model_name='action',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
