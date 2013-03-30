# -*- coding: utf-8 -*-
from osv import fields, osv

class mi_modulo_mi_tabla(osv.osv):
    _name = "mi_modulo.mi_tabla"
    _columns = {
        'name': fields.char('nombre', size=255, required=True, help='Coloque el nombre aquí', select=1),
        'active': fields.boolean('activo'),
        'quantity': fields.integer('cantidad'),
        'date': fields.date('fecha'),
        'datetime': fields.datetime('fecha y hora'),
        'description': fields.text('descripcion'),
        'price': fields.float('precio', digits = (10,4)),
        'options': fields.selection([('o1','opcion uno'),('o2','opcion dos')], 'opciones'),
    }
mi_modulo_mi_tabla()