# -*- coding: utf-8 -*-
from osv import fields, osv


################################################################################
#        ---  Objeto de negocio Libro
################################################################################
class biblioteca_libro(osv.osv):
        _name = "biblioteca.libro"
        _columns = {
            'active': fields.boolean('Active', help='Activo/Inactivo'),
            'isbn': fields.char('ISBN', size = 255),
            'titulo' : fields.char('Titulo', size = 255, help='Título del libro'),
            'autor' : fields.char('Autor', size = 255, help='Autor del libro'),
            'descripcion': fields.text('descripcion'),
            'paginas': fields.integer('Paginas'),
            'fecha': fields.date('Fecha', help='Fecha de publicación'),
            'precio': fields.float('Precio', help='Precio de compra'),
            'state': fields.selection([('draft', 'Draft'),('open', 'In Progress'),('cancel', 'Cancelled'),('done', 'Done'),('pending', 'Pending')],'State'),
        }
biblioteca_libro()