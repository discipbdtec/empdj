# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-06 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'departamento',
            },
        ),
        migrations.CreateModel(
            name='DepartamentoProjeto',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('numero_depto', models.ForeignKey(db_column='numero_depto', on_delete=django.db.models.deletion.DO_NOTHING, to='modulo1.Departamento')),
            ],
            options={
                'db_table': 'departamento_projeto',
            },
        ),
        migrations.CreateModel(
            name='Dependente',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome_dependente', models.CharField(blank=True, max_length=50, null=True)),
                ('nascimento', models.DateField(blank=True, null=True)),
                ('relacao', models.CharField(blank=True, max_length=10, null=True)),
                ('sexo', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'dependente',
            },
        ),
        migrations.CreateModel(
            name='Empregado',
            fields=[
                ('rg', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=50, null=True)),
                ('cpf', models.CharField(blank=True, max_length=10, null=True)),
                ('salario', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('dat_ini_sal', models.DateField(blank=True, null=True)),
                ('depto', models.ForeignKey(blank=True, db_column='depto', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='modulo1.Departamento')),
                ('rg_supervisor', models.ForeignKey(blank=True, db_column='rg_supervisor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='modulo1.Empregado')),
            ],
            options={
                'db_table': 'empregado',
            },
        ),
        migrations.CreateModel(
            name='EmpregadoProjeto',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('horas', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'empregado_projeto',
            },
        ),
        migrations.CreateModel(
            name='HistoricoSalario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_ini_sal', models.DateField()),
                ('dat_fim_sal', models.DateField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rg', models.ForeignKey(db_column='rg', on_delete=django.db.models.deletion.DO_NOTHING, to='modulo1.Empregado')),
            ],
            options={
                'db_table': 'historico_salario',
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=50, null=True)),
                ('localizacao', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'projeto',
            },
        ),
        migrations.AddField(
            model_name='empregadoprojeto',
            name='numero_projeto',
            field=models.ForeignKey(db_column='numero_projeto', on_delete=django.db.models.deletion.DO_NOTHING, to='modulo1.Projeto'),
        ),
        migrations.AddField(
            model_name='empregadoprojeto',
            name='rg_empregado',
            field=models.ForeignKey(db_column='rg_empregado', on_delete=django.db.models.deletion.DO_NOTHING, to='modulo1.Empregado'),
        ),
        migrations.AddField(
            model_name='dependente',
            name='rg_responsavel',
            field=models.ForeignKey(db_column='rg_responsavel', on_delete=django.db.models.deletion.DO_NOTHING, to='modulo1.Empregado'),
        ),
        migrations.AddField(
            model_name='departamentoprojeto',
            name='numero_projeto',
            field=models.ForeignKey(db_column='numero_projeto', on_delete=django.db.models.deletion.DO_NOTHING, to='modulo1.Projeto'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='rg_gerente',
            field=models.ForeignKey(blank=True, db_column='rg_gerente', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='modulo1.Empregado'),
        ),
    ]
