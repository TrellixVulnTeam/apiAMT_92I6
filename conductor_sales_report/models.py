from django.db import models

# Create your models here.

class conductor_sales_report(models.Model):
    company_id = models.CharField(verbose_name=('Nº Cooperativa'),
                            default='',
                            blank=True)
    company_name = models.CharField(verbose_name=('Nome de Cooperativa'),
                            default='',
                            blank=True)
    device = models.CharField(verbose_name=('Nº do Dispositivo'),
                            default='',
                            blank=True)
    conductor_id = models.CharField(verbose_name=('ID do Gestor'),
                            default='',
                            blank=True)
    conductor_first_name = models.CharField(verbose_name=('Matrícula do  Autocarro'),
                            max_length=4,
                            default='',
                            blank=True)
    conductor_last_name = models.CharField(verbose_name=('Nome do Gestor'),
                            max_length=4,
                            default='',
                            blank=True)
    number = models.CharField(verbose_name=('Total de passageiros'),
                            default='',
                            blank=True)
    amount = models.DecimalField(verbose_name=('Receita da Cooperativa'),
                            default='',
                            blank=True)
    date = models.DateField(verbose_name=('Data'),
                            blank=True,
                            null=True)

   