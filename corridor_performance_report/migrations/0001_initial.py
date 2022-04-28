# Generated by Django 3.2.9 on 2022-03-18 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index_translation', '0002_assign_bus_cooperative_corridor_routa'),
    ]

    operations = [
        migrations.CreateModel(
            name='corridor_performance_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('bus_nr', models.IntegerField(blank=True, default='', verbose_name='Nº de Autocarro')),
                ('spz', models.CharField(blank=True, default='', max_length=50, verbose_name='Matrícula')),
                ('operator', models.CharField(blank=True, default='', max_length=50, verbose_name='Gestor')),
                ('passenger_count', models.IntegerField(blank=True, null=True, verbose_name='Nº de Passageiros')),
                ('luggage_count', models.IntegerField(blank=True, null=True, verbose_name='Nº de Bagagem')),
                ('qr_ticket_count', models.IntegerField(blank=True, null=True, verbose_name='Nº de Tickets')),
                ('amount_ticket', models.DecimalField(blank=True, decimal_places=3, max_digits=30, null=True, verbose_name='Receita de Tickets')),
                ('amount_luggage', models.DecimalField(blank=True, decimal_places=3, max_digits=30, null=True, verbose_name='Receita de Bagagem')),
                ('maxcom_income', models.DecimalField(blank=True, decimal_places=3, max_digits=30, null=True, verbose_name='Receita da Maxcom')),
                ('amt_income', models.DecimalField(blank=True, decimal_places=3, max_digits=30, null=True, verbose_name='Receita da AMT')),
                ('operator_income', models.DecimalField(blank=True, decimal_places=3, max_digits=30, null=True, verbose_name='Receita da Cooperativa')),
                ('cooperative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corridorCooperative', to='index_translation.cooperative')),
                ('corridor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corridorCorridor', to='index_translation.corridor')),
                ('line_nr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corridorRouta', to='index_translation.routa')),
            ],
        ),
    ]