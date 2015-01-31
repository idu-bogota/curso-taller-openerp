# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.exceptions import ValidationError
from datetime import datetime
from datetime import timedelta
import random
import names

class biblioteca_libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Informacion de libro de la biblioteca'
    _order = 'sequence ASC, id DESC'

    _sql_constraints = [
        ('unique_isbn','unique(isbn)','El ISBN debe ser único'),
        ('precio_positivo','CHECK (precio >= 0)','El precio debe ser un valor positivo'),
    ]

    def _precio_aleatorio(self):
        return random.random()

    name = fields.Char('Titulo', size=255, help='Título del libro')
    active = fields.Boolean('Active', help='Activo/Inactivo', default=True)
    sequence = fields.Integer('Orden', help='Valor utilizado para ordenar el listado')
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
        help='Estado actual del libro en el catálogo',
        default='solicitud',
    )
    isbn = fields.Char(
        'ISBN', size=255,
        help="International Standard Book Number",
        copy=False
    )
    paginas = fields.Integer(
        'Número de Páginas',
        help="Número de páginas que tiene el libro",
    )
    fecha_compra = fields.Date(
        'Fecha de Compra',
        help="Fecha en la que se realizó la compra del libro",
        default=fields.Date.today
    )
    nombre_autor = fields.Char(
        'Nombre del Autor', size=255,
        help="Nombre completo del autor",
        default=names.get_full_name,
    )
    clasificacion = fields.Char(
        'Clasificación', size=255,
        help='Clasificación del libro',
    )
    genero = fields.Char(
        'Género', size=255,
        help='Género del libro',
    )
    editorial = fields.Char(
        'Editorial', size=255,
        help='Editorial del libro',
    )
    prestamo_ids = fields.One2many('biblioteca.prestamo', 'libro_id', 'Prestamos realizados')
    genero_ids = fields.Many2many('biblioteca.genero', string="Géneros")
    editorial_id = fields.Many2one('biblioteca.editorial', 'Editorial')
    autor_ids = fields.Many2many('biblioteca.autor', string='Autores')

    @api.one
    @api.constrains('fecha_publicacion','fecha_compra')
    @api.onchange('fecha_publicacion','fecha_compra')
    def _check_fechas(self):
        present = datetime.now()
        if self.fecha_compra and datetime.strptime(self.fecha_compra, '%Y-%m-%d') > present:
            raise ValidationError("Fecha de compra incorrecta")
        if self.fecha_publicacion and datetime.strptime(self.fecha_publicacion, '%Y-%m-%d') > present:
            raise ValidationError("Fecha de publicación incorrecta")

    @api.one
    @api.constrains('paginas')
    @api.onchange('paginas')
    def _check_paginas(self):
        if self.paginas < 0 or self.paginas > 5000:
            raise ValidationError("Un libro debe tener entre 0 y 5000 páginas")

    @api.onchange('precio')
    def onchange_precio(self):
        if self.precio and self.precio > 1000:
            self.descripcion = 'Ta muy caro el libro'

    @api.onchange('isbn')
    def onchange_warning_isbn(self):
        if self.isbn and len(self.isbn) < 10:
            self.descripcion = 'Verifique el ISBN cumpla con la norma'
            return {
                'warning': {
                    'title': "ISBN",
                    'message': "El largo del ISBN debe ser mayor o igual a 10 caracteres",
                }
            }

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
        compute='_compute_fecha_devolucion',
        inverse='_compute_inv_fecha_devolucion',
        store=False,
    )
    libro_id = fields.Many2one(
        'biblioteca.libro', 'Libro prestado',
        domain=[('state', '=', 'catalogado')],
        required=True,
    )
    editorial_id = fields.Many2one(
        related='libro_id.editorial_id',
        help="Editorial del libro prestado",
    )
    genero_ids = fields.Many2many(
        related='libro_id.genero_ids',
        readonly=True,
        string="Géneros del libro prestado",
    )

    @api.one
    def _compute_fecha_devolucion(self):
        """Calcula la fecha de devolución basado en la fecha inicial y la duración en días del prestamo"""
        if self.fecha and self.duracion_dias:
            fecha = fields.Datetime.from_string(self.fecha)
            self.fecha_devolucion = fecha + timedelta(days=self.duracion_dias)

    @api.one
    def _compute_inv_fecha_devolucion(self):
        """Calcula la fecha duración en días del prestamo basado en la fecha de devolución"""
        if self.fecha and self.fecha_devolucion:
            fecha = fields.Datetime.from_string(self.fecha)
            fecha_devolucion = fields.Datetime.from_string(self.fecha_devolucion)
            delta = fecha_devolucion - fecha
            self.duracion_dias = delta.days

class biblioteca_genero(models.Model):
    _name = 'biblioteca.genero'
    _description = 'Genero literario'

    name = fields.Char('Nombre', size=30, help='Nombre')
    libro_ids = fields.Many2many('biblioteca.libro', string="Libros")


class biblioteca_editorial(models.Model):
    _name = 'biblioteca.editorial'
    _description = 'Editorial de libro'

    name = fields.Char('Nombre', size=30, help='Nombre')
    libro_ids = fields.One2many('biblioteca.libro', 'editorial_id', 'Libros')


class biblioteca_autor(models.Model):
    _name = 'biblioteca.autor'
    _description = 'Autor de libro'

    name = fields.Char('Nombre', size=30, help='Nombre')
    libro_ids = fields.Many2many('biblioteca.libro', string='Libros')
