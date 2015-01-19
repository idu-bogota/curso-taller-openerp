# -*- coding: utf-8 -*-
from openerp import models, fields, api
import random

class biblioteca_libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Informacion de libro de la biblioteca'

    def _precio_aleatorio(self):
        return random.random()

    name = fields.Char('Titulo', size=255, help='Título del libro')
    active = fields.Boolean('Active', help='Activo/Inactivo', default=True)
    descripcion = fields.Text('Descripción')
    fecha_publicacion = fields.Date('Fecha de Publicación', help='Fecha de publicación', default=fields.Date.today)
    precio = fields.Float('Precio', help='Precio de Compra', digits=(10, 2), default=_precio_aleatorio)
    state = fields.Selection(
        [
            ('solicitud', 'Solicitado'),
            ('en_compra', 'Proceso de Compra'),
            ('adquirido', 'Adquirido'),
            ('catalogado', 'Catalogado'),
            ('baja', 'De Baja')
        ],
        'Estado',
        help='Estado actual del libro en el catálogo'
    )
    isbn = fields.Char(
        'ISBN', size=255,
        help="International Standard Book Number",
    )
    paginas = fields.Integer(
        'Número de Páginas',
        help="Número de páginas que tiene el libro",
    )
    fecha_compra = fields.Date(
        'Fecha de Compra',
        help="Fecha en la que se realizó la compra del libro",
    )
    nombre_autor = fields.Char(
        'Nombre del Autor', size=255,
        help="Nombre completo del autor",
    )

class biblioteca_prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'Informacion de prestamo de libros'

    fecha = fields.Datetime(
        'Fecha del Prestamo',
        help="Fecha en la que se presta el libro",
    )
    duracion_dias = fields.Integer(
        'Duración del Prestamo(días)',
        help="Número días por los cuales se presta el libro",
    )
    fecha_devolucion = fields.Datetime(
        'Fecha Devolución',
        help="Fecha de devolución del libro",
    )
