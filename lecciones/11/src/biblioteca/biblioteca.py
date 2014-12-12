# -*- coding: utf-8 -*-
from osv import fields, osv
from random import randint, random
from datetime import datetime

################################################################################
#        ---  Objeto de negocio Libro / Lección 9
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
        'state': fields.selection([('solicitud', 'Solicitado'),('compra', 'Proceso de compra'),
            ('adquirido', 'Adquirido'),('catalogado', 'Catalogado'),('baja', 'De baja')],'State'),
        'clasificacion_ids': fields.many2one('biblioteca.libro_clasificacion','Clasificación',
            select=True,
            ondelete='cascade'
        ),
        'genero_ids': fields.many2many('biblioteca.libro_genero','biblioteca_libro_generos',
                'genero_id',
                'libro_id',
                'Género del Libro',
        ),
        'editorial': fields.char('Editorial', size = 255, help='Editorial del libro'),
        'user_id': fields.many2one('res.users', 'Responsable de catalogar el libro',
                help= 'Profesional de biblioteca asignado para catalogar el libro'
        ),
        'prestamo_ids': fields.one2many('biblioteca.libro_prestamo', 'libro_id', 'Préstamo del libro'),
    }

    _sql_constraints = [
        ('unique_name','unique(titulo)','El nombre debe ser único'),
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
         'state': 'solicitud',
         'paginas': lambda *a: random(),
         'precio': _random_precio,
    }

    def onchange_active(self, cr, uid, ids, active):
       if not active:
           return {'value': {'state': 'baja'} }
       return {
           'warning': {'message': 'Cambiando el estado a "activo"'},
           'value': {'state': 'solicitud'},
       }

    def _get_name(self, cr, uid, ids, field, args, context=None):
        res = {}
        records = self.pool.get('plan_contratacion_idu.item').browse(cr, uid, ids, context=context)
        for record in records:
            res[record['id']] = "[{4}-{0}-{1}] {2} / {3} ({5})".format(record.dependencia_id.abreviatura,
                 record.id,
                 record.tipo_proceso_id.name,
                 record.tipo_proceso_seleccion_id.name,
                 record.plan_id.vigencia,
                 record.state,
             )
        return res

    def obtener_promedio_prestamo_metodo_read(self,cr,uid,ids,context=None):
        prestamo_ids = self.read(cr, uid, ids, ['prestamo_ids'], context=context)
        prestamo_pool = self.pool.get('biblioteca.libro_prestamo')
        prestamo_records = prestamo_pool.read(cr, uid, prestamo_ids[0]['prestamo_ids'], ['fecha_prestamo', 'fecha_regreso'], context=context)
        tiempo_total = 0
        for record in prestamo_records:
            tiempo_dias = (datetime.strptime(record['fecha_regreso'],'%Y-%m-%d') - datetime.strptime(record['fecha_prestamo'],'%Y-%m-%d')).days
            tiempo_total = tiempo_total + tiempo_dias
        raise osv.except_osv('Promedio de tiempo de préstamo','{0} días'.format(tiempo_total))
        return True

    def obtener_promedio_prestamo_metodo_browse(self,cr,uid,ids,context=None):
        prestamo_ids = self.read(cr, uid, ids, ['prestamo_ids'], context=context)
        prestamo_pool = self.pool.get('biblioteca.libro_prestamo')
        prestamo_records = prestamo_pool.browse(cr, uid, prestamo_ids[0]['prestamo_ids'], context=context)
        tiempo_total = 0
        for record in prestamo_records:
            tiempo_dias = (datetime.strptime(record['fecha_regreso'],'%Y-%m-%d') - datetime.strptime(record['fecha_prestamo'],'%Y-%m-%d')).days
            tiempo_total = tiempo_total + tiempo_dias
        raise osv.except_osv('Promedio de tiempo de préstamo','{0} días'.format(tiempo_total))
        return True

biblioteca_libro()

################################################################################
#        ---  Objeto de negocio libro_prestamo
################################################################################
class biblioteca_libro_prestamo(osv.osv):
    _name = "biblioteca.libro_prestamo"

    _columns = {
        'libro_id': fields.many2one('biblioteca.libro','id del Libro',
            select=True,
            ondelete='cascade'
        ),
        'fecha_prestamo': fields.date('Fecha de Préstamo'),
        'duracion_prestamo': fields.integer('días préstamo'),
        'fecha_regreso': fields.date('Fecha de Entrega'),
        'state': fields.selection([('prestado', 'Préstado'),('en_mora', 'En mora'),
            ('entregado', 'Entregado')],'State'),
        'user_id': fields.many2one('res.users', 'Usuario solicitante',
                help= 'Usuario que solicita el préstamo'
        ),
    }

biblioteca_libro_prestamo()

################################################################################
#        ---  Objeto de negocio libro_genero
################################################################################
class biblioteca_libro_genero(osv.osv):
    _name = "biblioteca.libro_genero"
    _columns = {
        'name': fields.char('Nombre Género'),
    }

biblioteca_libro_genero()

################################################################################
#        ---  Objeto de negocio libro_clasificacion
################################################################################
class biblioteca_libro_clasificacion(osv.osv):
    _name = "biblioteca.libro_clasificacion"
    _columns = {
       'name': fields.char('Clasificación'),
       'libro_id': fields.one2many('biblioteca.libro', 'clasificacion_ids', 'Clasificación del libro'),
    }

    _sql_constraints = [
        ('unique_name','unique(name)','El nombre debe ser único'),
    ]

biblioteca_libro_clasificacion()

################################################################################
#        ---  Objeto de negocio extendido de res.users
################################################################################
class res_users(osv.osv):
    _inherit = "res.users"
    _columns = {
       'prestamo_id'  : fields.one2many('biblioteca.libro_prestamo', 'user_id', 'Préstamos'),
    }

res_users()