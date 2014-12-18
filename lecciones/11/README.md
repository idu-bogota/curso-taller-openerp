[[
title: Lección 11: Wizards
author: STRT Grupo I+D+I
]]

Lección 11: Wizards
===================

[TOC]

Wizards
-------

Los Wizards son secuencias de interacción entre el cliente y el servidor. Para definir un wizard, se debe crear una clase que hereda de wizard.interface e instanciarla, cada wizard debe tener un nombre único.

¿Cómo adicionar un nuevo Wizard?
--------------------------------

1. Crear subdirectorio wizard en el módulo, adicionar el archivo __init__.py y el archivo .py para crear el wizard.
1. Adicionar el subdirectorio wizard a la lista de declaraciones de importación en el archivo __init__.py del módulo.
1. Adicionar el nombre del archivo .py en el archivo __init__.py del subdirectorio wizard.
1. Adicionar el archivo .xml para la vista del archivo .py
1. La acción que ejecuta el objeto debe ser: *<field name="target">new</field>*
1. Adicionar en el archivo _openerp_.py del módulo la vista .xml creada para el wizard, así:

		"data" : [
			'wizard/radicar_prestamo_view.xml',
			'biblioteca_view.xml',
		]


**Ejemplo de aplicación Wizard**:

Wizard para radicar un préstamo a un libro.

* **Crear archivo .py**

		 class biblioteca_wizard_radicar_prestamo(osv.osv_memory):
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


* **Crear archivo .xml**

		<?xml version="1.0"?>
		<openerp>
		<data>
			<!-- View Form Wizard -->
			<record id="view_biblioteca_wizard_radicar_prestamo" model="ir.ui.view">
				<field name="name">Radicar Prestamo</field>
				<field name="model">biblioteca.wizard.radicar_prestamo</field>
				<field name="type">form</field>
				<field name="arch" type="xml">
					<form string="Radicar Prestamo" version="7.0">
						<group colspan="2">
							<field name="libro_id" readonly="1"/>
							<field name="user_id"/>
							<field name="fecha_prestamo"/>
							<field name="duracion_prestamo"/>
						</group>
						<footer>
							<button name="action_radicar" string="Radicar solicitud" type="object" class="oe_highlight" />
						</footer>
					</form>
				</field>
			</record>

			<!-- Action  -->
			<record id="action_biblioteca_wizard_radicar_prestamo" model="ir.actions.act_window">
				<field name="name">Radicar Prestamo</field>
				<field name="type">ir.actions.act_window</field>
				<field name="res_model">biblioteca.wizard.radicar_prestamo</field>
				<field name="src_model">biblioteca.wizard.radicar_prestamo</field>
				<field name="view_id" ref="view_biblioteca_wizard_radicar_prestamo"/>
				<field name="view_type">form</field>
				<field name="view_mode">form</field>
				<field name="target">new</field>
			</record>
		</data>
		</openerp>

Ejercicios propuestos
---------------------

1. Revisar y registrar un préstamo a un libro utilizando el wizard de ejemplo.
