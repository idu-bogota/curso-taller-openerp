# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Instituto de Desarrollo Urbano (<http://www.idu.gov.co>).
#     All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import osv, fields
from openerp import netsvc


class biblioteca_wizard_radicar_prestamo(osv.osv_memory):
    """
    Wizard para radicar un préstamo al libro
    """
    _name = "biblioteca.wizard.radicar_prestamo"
    _description = "Permite radicar un prestamo"

    _columns={
        'libro_id': fields.many2one('biblioteca.libro_prestamo','Codigo préstamo',
             required=False,
             readonly=True,
         ),
        'fecha_prestamo': fields.date('Fecha de Préstamo'),
        'duracion_prestamo': fields.integer('días préstamo',
             required= True,
        ),
        'user_id': fields.many2one('res.users', 'Usuario solicitante',
             required= True,
             help= 'Usuario que solicita el préstamo'
        ),
    }

    _defaults = {
        'libro_id': lambda self, cr, uid, context : context['libro_id'] if context and 'libro_id' in context else None,
    }

    def action_radicar(self, cr, uid, ids, context=None):
        context['prestamo_actual'] = True
        form_id = ids and ids[0] or False
        form = self.browse(cr, uid, form_id, context=context)
        prestamo_pool = self.pool.get('biblioteca.libro_prestamo')
        vals = {
            'libro_id': form.libro_id.id,
            'state': 'prestado',
            'fecha_prestamo': form.fecha_prestamo,
            'duracion_prestamo': form.duracion_prestamo,
            'user_id': form.user_id.id
        }
        id = prestamo_pool.create(cr, uid, vals, context=context)
        return self.redirect_to_prestamo_view(cr, uid, id, context=context)

    def redirect_to_prestamo_view(self, cr, uid, id, context=None):
        return {
            'name': 'Radicar Prestamo',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'biblioteca.libro_prestamo',
            'res_id': int(id),
            'type': 'ir.actions.act_window',
        }

biblioteca_wizard_radicar_prestamo()
