# -*- coding: utf-8 -*-
from osv import fields, osv
from random import randint, random
from datetime import datetime


################################################################################
#        ---  Objeto de negocio Libro
################################################################################
class biblioteca_libro(osv.osv):
    _name = "biblioteca.libro"
    _order= 'fecha'
    _columns = {
        'active': fields.boolean('Active', help='Activo/Inactivo'),
        'isbn': fields.char('ISBN', size = 255, required=True,),
        'titulo' : fields.char('Titulo', size = 255, help='Título del libro'),
        'autor' : fields.char('Autor', size = 255, help='Autor del libro'),
        'descripcion': fields.text('descripcion'),
        'paginas': fields.integer('Paginas'),
        'fecha': fields.date('Fecha', help='Fecha de publicación'),
        'precio': fields.float('Precio',  digits = (10,4), help='Precio de compra'),
        'state': fields.selection([('draft', 'Draft'),('open', 'In Progress'),('cancel', 'Cancelled'),('done', 'Done'),('pending', 'Pending')],'State'),
        'clasificacion': fields.char('Clasificación', size = 255, help='Clasificación del libro'),
        'genero': fields.char('Género', size = 255, help='Género del libro'),
        'editorial': fields.char('Editorial', size = 255, help='Editorial del libro'),
    }

    _sql_constraints = [
        ('unique_name','unique(name)','El nombre debe ser único'),
    ]

    def _check_fecha(self, cr, uid, ids, context = None):
        is_valid_data = True
        present = datetime.now()
        for obj in self.browse(cr,uid,ids,context=None):
            if not obj.fecha:
                continue
            date = datetime.strptime(obj.fecha, '%Y-%m-%d')
            if(date > present):
                is_valid_data = False
        return is_valid_data

    _constraints = [
        (_check_fecha,'Fecha debe ser anterior a la fecha actual',['fecha']),
    ]

    def _random_precio(self, cr, uid, context = None):
        return randint(5,100)

    _defaults = {
         'active': True,
         'state': 'draft',
         'paginas': lambda *a: random(),
         'precio': _random_precio,
    }
biblioteca_libro()

################################################################################
#        ---  Objeto de negocio libro_prestamo
################################################################################
class biblioteca_libro_prestamo(osv.osv):
    _name = "biblioteca.libro_prestamo"
    _columns = {
        'fecha_prestamo': fields.date('Fecha de Préstamo'),
        'duracion_prestamo': fields.integer('días préstamo'),
        'fecha_regreso': fields.date('Fecha de Entrega'),
    }
biblioteca_libro_prestamo()