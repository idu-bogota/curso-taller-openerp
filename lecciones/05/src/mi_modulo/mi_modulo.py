# -*- coding: utf-8 -*-
from osv import fields, osv
from random import randint, random
from datetime import datetime

class mi_modulo_mi_tabla(osv.osv):
    _name = "mi_modulo.mi_tabla"
    _order= 'name'
    _columns = {
        'name': fields.char('nombre', size=255, required=True, help='Coloque el nombre aquí', select=1),
        'active': fields.boolean('activo'),
        'quantity': fields.integer('cantidad'),
        'date': fields.date('fecha'),
        'datetime': fields.datetime('fecha y hora'),
        'description': fields.text('descripcion'),
        'price': fields.float('precio', digits = (10,4)),
        'tabla_relacionada_id': fields.many2one('mi_modulo.mi_tabla_relacionada', 'Tabla Relacionada', domain="[('state','=','active')]", ondelete='set null'),
        'partner_ids': fields.many2many('res.partner', 'mi_modulo_partner_rel', 'mi_tabla_id', 'partner_id', 'Proveedores'),
        'state': fields.selection([('draft','borrador'),('active','Activo'),('cancelled','Cancelado')], 'estado', required=True),
    }

    _sql_constraints = [
        ('unique_name','unique(name)','El nombre debe ser único'),
    ]

    def _check_date(self, cr, uid, ids, context = None):
        is_valid_data = True
        present = datetime.now()
        for obj in self.browse(cr,uid,ids,context=None):
            if not obj.date or not obj.datetime:
                continue

            date = datetime.strptime(obj.date, '%Y-%m-%d')
            date_time = datetime.strptime(obj.datetime, '%Y-%m-%d %H:%M:%S')
            if(date < present or date_time < present):
                is_valid_data = False

        return is_valid_data

    _constraints = [
        (_check_date,'Fecha debe ser en el futuro',['date','datetime']),
    ]

    def _random_quantity(self, cr, uid, context = None):
        return randint(5,100)

    _defaults = {
         'active': True,
         'state': 'draft',
         'price': lambda *a: random(),
         'quantity': _random_quantity,
    }
    
mi_modulo_mi_tabla()


class mi_modulo_mi_tabla_relacionada(osv.osv):
    _name = "mi_modulo.mi_tabla_relacionada"
    _columns = {
        'name': fields.char('nombre', size=255, required=True, help='Coloque el nombre aquí', select=1),
        'active': fields.boolean('activo'),
        'state': fields.selection([('draft','borrador'),('active','Activo'),('cancelled','Cancelado')], 'estado', required=True),
        'related': fields.one2many('mi_modulo.mi_tabla', 'tabla_relacionada_id', 'Objetos relacionados'),
    }
    _defaults = {
         'active': True,
         'state': 'draft',
    }

mi_modulo_mi_tabla_relacionada()