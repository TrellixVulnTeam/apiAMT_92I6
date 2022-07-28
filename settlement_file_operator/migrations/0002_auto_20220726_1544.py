# Generated by Django 3.2.9 on 2022-07-26 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index_translation', '0003_alter_manager_user'),
        ('settlement_file_operator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settlement_file_operator',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='settlement_file_operator',
            name='cooperatives',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='settlementCooperative', to='index_translation.cooperative'),
        ),
    ]
