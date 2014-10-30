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
        'clasificacion': fields.char('Clasificacion', size = 255, help='Clasificación del libro'),
        'genero': fields.char('Género', size = 255, help='Género del libro'),
        'editorial': fields.char('Editorial', size = 255, help='Editorial del libro'),
    }
biblioteca_libro()

################################################################################
#        ---  Objeto de negocio libro_prestamo
################################################################################
class biblioteca_libro_prestamo(osv.osv):
    _name = "biblioteca.libro_prestamo"
    _columns = {
        'fecha_prestamo': fields.date('Fecha de Préstamo'),
        'duración_prestamo': fields.integer('días préstamo'),
        'fecha_regreso': fields.date('Fecha de Entrega'),
    }
biblioteca_libro_prestamo()