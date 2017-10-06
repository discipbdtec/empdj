# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Empregado,Departamento,DepartamentoProjeto,Projeto,EmpregadoProjeto,HistoricoSalario,Dependente

admin.site.register(Empregado)
admin.site.register(Departamento)
admin.site.register(Projeto)
admin.site.register(HistoricoSalario)
admin.site.register(Dependente)
admin.site.register(EmpregadoProjeto)
admin.site.register(DepartamentoProjeto)
