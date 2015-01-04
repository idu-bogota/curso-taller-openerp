# -*- coding: utf-8 -*-
from openerp import models, fields


class mi_modulo_mi_tabla(models.Model):
    _name = "mi_modulo.mi_tabla"

    name = fields.Char('Nombre', size=25)
    description = fields.Char('Descripción', size=255)
