# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Departamento(models.Model):
    numero = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    rg_gerente = models.ForeignKey('Empregado', models.DO_NOTHING, db_column='rg_gerente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'


class DepartamentoProjeto(models.Model):
    codigo = models.AutoField(primary_key=True)
    numero_depto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='numero_depto')
    numero_projeto = models.ForeignKey('Projeto', models.DO_NOTHING, db_column='numero_projeto')

    class Meta:
        managed = False
        db_table = 'departamento_projeto'


class Dependente(models.Model):
    codigo = models.AutoField(primary_key=True)
    rg_responsavel = models.ForeignKey('Empregado', models.DO_NOTHING, db_column='rg_responsavel')
    nome_dependente = models.CharField(max_length=50, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    relacao = models.CharField(max_length=10, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dependente'


class Empregado(models.Model):
    rg = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    cpf = models.CharField(max_length=10, blank=True, null=True)
    depto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='depto', blank=True, null=True)
    rg_supervisor = models.ForeignKey('self', models.DO_NOTHING, db_column='rg_supervisor', blank=True, null=True)
    salario = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    dat_ini_sal = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empregado'


class EmpregadoProjeto(models.Model):
    codigo = models.AutoField(primary_key=True)
    rg_empregado = models.ForeignKey(Empregado, models.DO_NOTHING, db_column='rg_empregado')
    numero_projeto = models.ForeignKey('Projeto', models.DO_NOTHING, db_column='numero_projeto')
    horas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empregado_projeto'


class HistoricoSalario(models.Model):
    rg = models.ForeignKey(Empregado, models.DO_NOTHING, db_column='rg')
    dat_ini_sal = models.DateField()
    dat_fim_sal = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'historico_salario'


class Projeto(models.Model):
    numero = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    localizacao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projeto'
