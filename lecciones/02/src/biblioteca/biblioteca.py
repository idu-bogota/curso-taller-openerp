# -*- coding: utf-8 -*-
from openerp import models, fields


class biblioteca_libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Contiene la informacion de libros en la biblioteca'

    name = fields.Char('Titulo', size=255, help='Título del libro')
    active = fields.Boolean('Active', help='Activo/Inactivo')
    descripcion = fields.Text('Descripción')
    fecha_publicacion = fields.Date('Fecha', help='Fecha de publicación')
    precio = fields.Float('Precio', help='Precio de compra', digits=(10, 2))
    state = fields.Selection(
        [
            ('catalogado', 'Catalogado'),
            ('baja', 'De baja')
        ],
        'Estado',
    )
