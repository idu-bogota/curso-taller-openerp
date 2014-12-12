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
1. Adicionar el subdirectorio wizard a la lista de declaraciones de importación en el archivo __init__.py del módulo,
1. Adicionar el nombre del archivo .py en el archivo __init__.py del subdirectorio wizard.
1. Adicionar el archivo .xml para la vista del archivo .py
1. La acción que ejecuta el objeto debe ser: *<field name="target">new</field>*


**Ejemplo de aplicación Wizard**:

Wizard para radicar un préstamo a un libro.

* **Crear archivo .py**

		class biblioteca_libro_wizard_prestamo(osv.osv_memory):
		_name = "biblioteca_libro.wizard.prestamo"
		_description = "Permite radicar un prestamo"

		_columns={
				'libro_id': fields.many2one('biblioteca.libro_prestamo','Item a cambiar/eliminar',
					 required=False,
					 readonly=True,
				 ),
		}

		_defaults = {
			'libro_id': lambda self, cr, uid, context : context['libro_id'] if context and 'libro_id' in context else None,
		}

		def action_radicar(self, cr, uid, ids, context=None):
			context['prestamo_actual'] = True
			form_id = ids and ids[0] or False
			form = self.browse(cr, uid, form_id, context=context)
			prestamo_pool = self.pool.get('biblioteca_libro.prestamo')
			vals = {
				'libro_id': form.libro_id.id,
				'state': 'prestado',
			}

			id = prestamo_pool.create(cr, uid, vals, context=context)
			return self.redirect_to_prestamo_view(cr, uid, id, context=context)

		def redirect_to_prestamo_view(self, cr, uid, id, context=None):
			return {
				'name': 'Radicar Prestamo',
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': 'biblioteca_libro.prestamo',
				'res_id': int(id),
				'type': 'ir.actions.act_window',
			}
		biblioteca_libro_wizard_prestamo()


* **Crear archivo .xml**

		<!-- View Form Wizard -->
		<record id="view_biblioteca_libro_wizard_prestamo" model="ir.ui.view">
			<field name="name">Radicar Prestamo</field>
			<field name="model">biblioteca_libro.wizard.prestamo</field>
			<field name="type">form</field>
			<field name="arch" type="xml">
				<form string="Radicar Prestamo" version="7.0">
					<group col="4">
						<field name="libro_id" colspan="4" readonly="1"/>
					</group>
					<footer>
						<button name="action_radicar" string="Radicar solicitud" type="object" class="oe_highlight" />
					</footer>
				</form>
			</field>
		</record>

		<!-- Action  -->
		<record id="action_biblioteca_libro_wizard_prestamo" model="ir.actions.act_window">
			<field name="name">Radicar Prestamo</field>
			<field name="type">ir.actions.act_window</field>
			<field name="res_model">biblioteca_libro.wizard.prestamo</field>
			<field name="src_model">biblioteca_libro.wizard.prestamo</field>
			<field name="view_id" ref="view_biblioteca_libro_wizard_prestamo"/>
			<field name="view_type">form</field>
			<field name="view_mode">form</field>
			<field name="target">new</field>
		</record>

Ejercicios propuestos
---------------------

1. Revisar y registrar un préstamo a un libro utilizando el wizard de ejemplo.
